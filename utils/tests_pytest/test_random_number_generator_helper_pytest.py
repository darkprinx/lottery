import uuid


from utils.helpers.random_number_generator_helper import generate_customized_uuid


def test_generate_customized_uuid_with_prefix(monkeypatch):
    fixed = "3d84jx83ks9ss98lk92jasrcmsis93"
    monkeypatch.setattr(uuid, "uuid4", lambda: fixed)

    assert generate_customized_uuid("1") == f"1-{fixed}"


def test_generate_customized_uuid_without_prefix(monkeypatch):
    fixed = "3d84jx83ks9ss98lk92jasrcmsis93"
    monkeypatch.setattr(uuid, "uuid4", lambda: fixed)

    assert generate_customized_uuid() == fixed


def test_generate_customized_uuid_is_random():
    # Very small probability of collision; this just ensures it usually differs from a specific fixed string
    not_expected = "3d84jx83ks9ss98lk92jasrcmsis93"
    assert generate_customized_uuid() != not_expected
