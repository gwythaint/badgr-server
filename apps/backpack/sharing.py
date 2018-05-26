import urllib

from django.conf import settings


class ShareProvider(object):
    provider_code = None

    def __init__(self, provider):
        self.provider = provider


class TwitterShareProvider(ShareProvider):
    provider_code = 'twitter'
    provider_name = 'Twitter'

    def share_url(self, badge_instance, **kwargs):
        return "https://twitter.com/intent/tweet?text={url}".format(
            url=urllib.quote(badge_instance.share_url)
        )


class FacebookShareProvider(ShareProvider):
    provider_code = 'facebook'
    provider_name = 'Facebook'

    def share_url(self, badge_instance, **kwargs):
        return "https://www.facebook.com/sharer/sharer.php?u={url}".format(
            url=urllib.quote(badge_instance.share_url)
        )


class PortfoliumShareProvider(ShareProvider):
    provider_code = 'portfolium'
    provider_name = 'Portfolium'
    source_name = "Badgr"

    def get_source_name(self):
        return self.source_name

    def share_url(self, badge_instance, **kwargs):
        return "https://portfolium.com/share/badge?source={source}&u={url}".format(
            url=urllib.quote(badge_instance.share_url),
            source=self.get_source_name()
        )


class LinkedinShareProvider(ShareProvider):
    provider_code = 'linkedin'
    provider_name = 'LinkedIn'

    def share_url(self, instance, **kwargs):
        url = None
        # sharing as a certification is broken so disabling for now [Wiggins june 2017]
        # if hasattr(instance, 'cached_badgeclass'):
        #     url = self.certification_share_url(instance, **kwargs)

        if not url:
            url = self.feed_share_url(instance, **kwargs)
        return url

    def feed_share_url(self, badge_instance, title=None, summary=None):
        if title is None:
            title = "I earned a badge from Badgr!"
        if summary is None:
            summary = badge_instance.cached_badgeclass.name,
        return "https://www.linkedin.com/shareArticle?mini=true&url={url}&title={title}&summary={summary}".format(
            url=urllib.quote(badge_instance.share_url),
            title=title,
            summary=summary
        )

    def certification_share_url(self, badge_instance, **kwargs):
        cert_issuer_id = getattr(settings, 'LINKEDIN_CERTIFICATION_ISSUER_ID', None)
        if cert_issuer_id is None:
            return None
        return "https://www.linkedin.com/profile/add?_ed={certIssuerId}&pfCertificationName={name}&pfCertificationUrl={url}".format(
            certIssuerId=cert_issuer_id,
            name=urllib.quote(badge_instance.cached_badgeclass.name),
            url=urllib.quote(badge_instance.share_url)
        )


class SharingManager(object):
    provider_code = None
    ManagerProviders = {
        FacebookShareProvider.provider_code: FacebookShareProvider,
        LinkedinShareProvider.provider_code: LinkedinShareProvider,
        TwitterShareProvider.provider_code: TwitterShareProvider,
        PortfoliumShareProvider.provider_code: PortfoliumShareProvider,
    }

    @classmethod
    def share_url(cls, provider, badge_instance, **kwargs):
        manager_cls = SharingManager.ManagerProviders.get(provider.lower(), None)
        if manager_cls is None:
            raise NotImplementedError(u"Provider not supported: {}".format(provider))
        manager = manager_cls(provider)
        url = manager.share_url(badge_instance, **kwargs)
        return url

    @classmethod
    def is_provider_supported(cls, provider):
        return provider in SharingManager.ManagerProviders
