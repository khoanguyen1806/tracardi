# from uuid import uuid4

from typing import List

from tracardi.domain.system_entity_property import SystemEntityProperty

default_profile_properties: List[SystemEntityProperty] = [
    SystemEntityProperty(entity='profile', id='48be9511-7873-4e5a-aae1-cf62216e43c5', property='id', type='string', optional=False, default=None),
    SystemEntityProperty(entity='profile', id='90b98e78-fb16-45ba-8691-081e06d1ca2b', property='ids', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='72da7d73-d22b-4dfa-bb54-cec669292e1f', property='metadata.time.insert', type='datetime', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='80d5979a-7bb5-4768-9a79-02dc3c740244', property='metadata.time.create', type='datetime', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='19ae8b3a-ef2e-4347-ba99-0b0e1c81f80d', property='metadata.time.update', type='datetime', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='d20af14d-bb6f-44b8-a41f-040aca7842fc', property='operation.new', type='bool', optional=True, default='False'),
    SystemEntityProperty(entity='profile', id='16511736-2413-4f5a-9c5c-7db6ad8aa390', property='operation.update', type='bool', optional=True, default='False'),
    SystemEntityProperty(entity='profile', id='cec510f0-d4e9-4061-bb21-e92aaa8f10cd', property='stats.visits', type='integer', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='68be2a45-f71e-4416-923e-2544f6af727d', property='stats.views', type='integer', optional=False, default='0'),
    SystemEntityProperty(entity='profile', id='4e2606f4-06a4-4449-8335-4290042835a6', property='stats.counters', type='dict', optional=False, default='{}'),
    SystemEntityProperty(entity='profile', id='d28cd5bb-6390-4b41-97b4-d0d1818c1e75', property='traits', type='dict', optional=True, default='{}'),
    SystemEntityProperty(entity='profile', id='73bc2894-0164-40b0-9684-8492c1ab31ae', property='segments', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='4b7c196a-d546-4e82-b74a-7d4e0fe41ab1', property='interests', type='dict', optional=True, default='{}'),
    SystemEntityProperty(entity='profile', id='ae3c5af2-9a38-4bd6-b89f-7cd242262edb', property='consents', type='Dict[str, ConsentRevoke]', optional=True, default='{}'),
    SystemEntityProperty(entity='profile', id='72144715-de3b-4a2f-915b-77d745d73d7c', property='active', type='bool', optional=False, default='True'),
    SystemEntityProperty(entity='profile', id='ef46fe0a-7f24-4757-a0e4-4dd23c432467', property='aux', type='dict', optional=True, default='{}'),
    SystemEntityProperty(entity='profile', id='385e06a8-9204-4c72-8e45-bd12369d389c', property='data.anonymous', type='bool', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='ad6d03af-c223-48f4-b675-650949d8d484', property='data.pii.firstname', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='1da7eecd-9938-4f8e-9329-d2e50524c621', property='data.pii.lastname', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='c013d36a-0a56-4ee9-9956-1a9d9b160946', property='data.pii.display_name', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='e81247b4-ae65-4213-86ee-23159ec1a8f3', property='data.pii.birthday', type='datetime', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='5e5acb0a-66d7-4c64-ae63-183f0c716368', property='data.pii.language.native', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='fb0606ed-f5e5-45d7-aeb3-9956b74c35cf', property='data.pii.language.spoken', type='List[str]', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='a5418ca9-ac17-4bce-84c8-0cc43c51cf00', property='data.pii.gender', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='64c4a9f8-6118-497e-836a-d29c1d3ee2c7', property='data.pii.education.level', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='56053f73-23a5-4282-89bf-8f444e6b85f0', property='data.pii.civil.status', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='68d6432e-a2f2-4ccb-b954-eba34cbae7bf', property='data.pii.attributes.height', type='float', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='6b9c4f78-c49f-4fa4-87d2-63591d765a52', property='data.pii.attributes.weight', type='float', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='7121a191-fdcd-4fd0-bf9f-3d9b6cdaead3', property='data.pii.attributes.shoe_number', type='float', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='6c0dcd60-fde5-4c9e-b68a-e1b1425fc327', property='data.contact.email.main', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='3a614157-5c60-4cbe-83f9-894b9f29de1f', property='data.contact.email.private', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='46b19c1c-07f1-40d7-bf30-0186cb5befb3', property='data.contact.email.business', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='7dba41ab-0cb8-4d60-969d-21313c37db54', property='data.contact.phone.main', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='0b15236d-17a8-40c5-9d75-037063cf8f18', property='data.contact.phone.business', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='974a233f-eb77-4ca5-86d0-f25b2ac2acaf', property='data.contact.phone.mobile', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='46be4d30-1483-49e7-b0df-063e5f3117a9', property='data.contact.phone.whatsapp', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='16f62299-8bb5-4f1a-843d-d463a6771a5c', property='data.contact.app.whatsapp', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='e0a5641f-7e90-406d-8284-cf43c80c2e2c', property='data.contact.app.discord', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='800c472c-9133-4f86-ace8-b970a5758d50', property='data.contact.app.slack', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='531518e8-92bc-42b3-a661-fa0dea72a8c5', property='data.contact.app.twitter', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='5f3f80bf-5d07-454a-8d53-17efced18906', property='data.contact.app.telegram', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='28c5a0cf-b818-440f-8d78-17f53ff8ce25', property='data.contact.app.wechat', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='29a3a66a-a88b-41d3-a304-2c3bf6d04d56', property='data.contact.app.viber', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='93f4e2c7-8f65-41b4-afea-65d5bc05652f', property='data.contact.app.signal', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='560c5a1f-25e4-4e6b-b8a8-9a7050ceba55', property='data.contact.address.town', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='eac3170e-7e0a-473c-b4d5-2657fe65f5f5', property='data.contact.address.county', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='6eedc4fc-72e7-44dd-80b6-df2233858f07', property='data.contact.address.country', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='69a1e665-c472-47ee-8e48-f3dc9ea91cfe', property='data.contact.address.postcode', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='56e7371a-f07a-46b9-abf7-568052a1773d', property='data.contact.address.street', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='6af97951-54f8-4e5c-a619-d44a3acb7b38', property='data.contact.address.other', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='bccfcc23-c817-47ac-8f82-13c8096fd82c', property='data.identifier.id', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='eda6f0c7-ebbc-4f41-963d-a98aaf4ed01c', property='data.identifier.pk', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='4b8f474c-ab5f-4b95-b644-86ff8889423d', property='data.identifier.badge', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='e769c9b9-ee81-44c7-b8ec-20defefc7478', property='data.identifier.passport', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='5b794097-e360-4023-b272-8d48e64a34cb', property='data.identifier.credit_card', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='754b36e3-69ae-4f07-ba54-e3efe9d9e342', property='data.identifier.token', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='6d051b80-347a-447c-be9f-75e878e380c4', property='data.identifier.coupons', type='List[str]', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='5acb73b7-da38-4c9a-b713-bc055be079df', property='data.media.image', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='442ee0ad-93a1-404d-ae9c-5bb0cddc349b', property='data.media.webpage', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='9ec4a2a1-46b5-4f3e-8165-d23291046c8c', property='data.media.social.twitter', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='b5ff2867-d8d9-4467-a921-2821ee9adfc0', property='data.media.social.facebook', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='0e8ae744-a37a-48b7-8fd8-de6f3025beaa', property='data.media.social.youtube', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='c3d02ec0-f8ff-434e-96cb-97539b07d8af', property='data.media.social.instagram', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='a25673ad-dc68-4a6a-b654-53d15da81046', property='data.media.social.tiktok', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='d8a21e31-3a21-4133-a944-ea028a010477', property='data.media.social.linkedin', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='68715af8-7c05-4b43-b57c-7a449b74c73c', property='data.media.social.reddit', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='e7e3c6ca-f61a-4444-949c-6e02b7d3cc31', property='data.media.social.other', type='dict', optional=True, default='{}'),
    SystemEntityProperty(entity='profile', id='db1f7f98-30fe-4082-beab-a816a43264f5', property='data.preferences.purchases', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='9ba0d923-e040-4a3c-b049-24d503abbbee', property='data.preferences.colors', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='567e7d26-5be2-43e0-9427-c10bc5f75044', property='data.preferences.sizes', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='07bab6d0-263c-4999-a5d2-205c88d3daae', property='data.preferences.devices', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='63b9bf46-6ad3-4ac1-ac98-fb0886a38aaa', property='data.preferences.channels', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='e96d6dc4-024b-4d44-a8ef-e20a38aed394', property='data.preferences.payments', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='ccc7f7b4-856f-46e3-aacb-d9c8437aa218', property='data.preferences.brands', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='d0c96de4-67a7-4cc2-952d-596eede1d695', property='data.preferences.fragrances', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='80181d7d-99e4-4fb7-9c5b-81d537a41390', property='data.preferences.services', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='b58c4484-2900-4de4-9c78-884053c1502e', property='data.preferences.other', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='1dc6070b-cddc-494b-92ba-a1247e3bd0cb', property='data.job.position', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='6b1cffb9-9e84-43b2-9dd0-e127bf1af73d', property='data.job.salary', type='float', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='c2150f5e-99c2-4100-8a8a-4aebb37778ed', property='data.job.type', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='3cfd8c36-36e9-4e92-88fd-f332e97e1ee8', property='data.job.company.name', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='083fafcc-1d30-4101-823e-b744368d48b1', property='data.job.company.size', type='int', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='7859ff38-c4fd-4dd4-a051-a9ed725bdf38', property='data.job.company.segment', type='List[str]', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='1678886e-c92f-4a31-ac4a-d0f778333df4', property='data.job.company.country', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='5b7c5e18-d481-4a7d-8bc7-6552f7b0de35', property='data.job.department', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='d986bad5-da8e-4e9d-ad2d-bc17380ff908', property='data.metrics.ltv', type='float', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='be6c917b-ddef-4cad-8fcc-9f28fc089fb9', property='data.metrics.ltcosc', type='int', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='3c8c4d87-0039-4e13-8500-5e8a3e1bec46', property='data.metrics.ltcocc', type='int', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='a3ab1c3c-2708-4b77-b4a7-7f95f5289938', property='data.metrics.ltcop', type='float', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='4ce31981-2735-4520-80ad-081a842e3339', property='data.metrics.ltcosv', type='float', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='69717dd1-281a-4289-aca4-0d81b3f15e30', property='data.metrics.ltcocv', type='float', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='43fd4e40-90d9-44ce-8b1f-a947465439ef', property='data.metrics.next', type='datetime', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='02fee5f3-76e9-4422-b705-212087453c91', property='data.metrics.custom', type='dict', optional=True, default='{}'),
    SystemEntityProperty(entity='profile', id='7272384a-765a-4ec7-a92c-8eaa196f0d4c', property='data.loyalty.codes', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='6b26b032-b96e-4e93-9d79-d693aefba233', property='data.loyalty.card.id', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='a344e194-a984-4a18-8f1a-ba8e9edb0c4e', property='data.loyalty.card.name', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='437b4a1e-ba6a-4795-a2b1-8c9fe9f303bc', property='data.loyalty.card.issuer', type='string', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='d55adc4b-028a-413b-b9f4-2ccef49ec277', property='data.loyalty.card.expires', type='datetime', optional=True, default='NULL'),
    SystemEntityProperty(entity='profile', id='03421596-29dd-4b6c-9dc5-edb5b4cc5718', property='data.loyalty.card.points', type='float', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='5979d815-2f76-4753-806b-a4d58de73863', property='data.devices.push', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='d14f5de6-90be-498e-93ed-bf8d63d98ca1', property='data.devices.other', type='List[str]', optional=True, default='[]'),
    SystemEntityProperty(entity='profile', id='78144375-87ee-49da-bbea-09874c2cd71b', property='data.devices.last.geo.location', type='Tuple[float,float]', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='3e7aedbd-7597-4897-8b18-3e408f8a917a', property='data.devices.last.geo.longitude', type='float', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='cdf12474-d8da-4bfb-b132-78ffcbcc9ab1', property='data.devices.last.geo.latitude', type='float', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='8ed513bf-e2a3-4124-970f-f2287c69fe4d', property='data.devices.last.geo.postal', type='string', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='1999c6bd-31fa-4a38-aca3-6e240a148d9b', property='data.devices.last.geo.county', type='string', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='7bfeb655-e063-4cb2-873c-a5ffa3430f2b', property='data.devices.last.geo.city', type='string', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='437074e7-0756-45d4-8583-7c6880cf927a', property='data.devices.last.geo.country.code', type='string', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='b1a6b611-f033-4495-8b25-03b2003b587a', property='data.devices.last.geo.country.name', type='string', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='6b79adb3-d76b-438c-9bbb-fafca580647b', property='data.contact.confirmations', type='List[str]', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='dc0e8e9a-eb71-4097-9f40-10fedca217c4', property='stats.views', type='integer', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='1520bae5-6b23-47ac-8052-335a2acb1d0f', property='stats.visits', type='integer', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='6381ab1f-9b42-4548-9c9e-f1482b40e079', property='operation.merge', type='List[str]', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='a39c5c52-4fe0-4632-bafb-4accdb31313d', property='operation.segment', type='bool', optional=True, default='false'),
    SystemEntityProperty(entity='profile', id='e61938e1-21de-46bf-8cfc-f89070e60623', property='metadata.status', type='string', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='468e24a2-b314-4476-bbbe-51e816068986', property='metadata.time.visit.tz', type='string', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='e64fe226-ab27-4c8c-9978-9f9f8310a3cd', property='metadata.time.visit.count', type='integer', optional=True, default='0'),
    SystemEntityProperty(entity='profile', id='8f682e20-04ff-48da-9f7c-141c614d9b91', property='metadata.time.visit.current', type='datetime', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='61d9747e-090a-4a76-b902-f462230d21a8', property='metadata.time.visit.last', type='datetime', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='d7026962-5828-47a6-9f9d-bb276d80a324', property='metadata.time.segmentation', type='datetime', optional=True, default=None),
    SystemEntityProperty(entity='profile', id='8b79c364-ab9d-4967-ac90-b98aba0c7ed2', property='primary_id', type='string', optional=True, default='NULL'),
]


# for x in default_profile_properties:
#     print(
# f"""SystemEntityProperty(entity='profile', id='{uuid4()}', property='{x.id}', type='{x.type}', optional={x.optional}, default={f"'{x.default}'" if x.default is not None else None}),"""
#     )