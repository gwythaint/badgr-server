from celery.utils.log import get_task_logger

import badgrlog
from badgeuser.models import CachedEmailAddress
from mainsite.celery import app

logger = get_task_logger(__name__)
badgrLogger = badgrlog.BadgrLogger()


@app.task(bind=True)
def process_email_verification(self, email_address_id):
    from issuer.models import BadgeInstance
    try:
        email_address = CachedEmailAddress.cached.get(id=email_address_id)
    except CachedEmailAddress.DoesNotExist:
        return

    user = email_address.user
    issuer_instances = BadgeInstance.objects.filter(recipient_identifier=email_address.email)
    variants = list(email_address.cached_variants())

    for i in issuer_instances:
        if i.recipient_identifier not in variants and \
                i.recipient_identifier != email_address.email and \
                user.can_add_variant(i.recipient_identifier):
            email_address.add_variant(i.recipient_identifier)

            variants.append(i.recipient_identifier)
