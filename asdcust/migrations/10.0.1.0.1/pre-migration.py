# -*- coding: utf-8 -*-


def migrate(cr, version):

    if not version:
        return

    cr.execute("""

               INSERT INTO "res_partner" (
                    "id", "customer", "lang", "tz", "name", "color",
                    "company_id", "partner_share", "supplier", "employee",
                    "active", "type", "is_company", "create_uid", "write_uid",
                    "create_date", "write_date")
               VALUES(
                    nextval('res_partner_id_seq'), true, 'en_US', NULL,
                    'Agrolait', 0, 1, false, false, false, true, 'contact',
                    false, 1, 1, (now() at time zone 'UTC'),
                    (now() at time zone 'UTC'))

               """)
