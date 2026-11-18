from app.core.security import hash_password, needs_rehash, verify_password


def test_hash_is_not_plaintext_and_is_argon2id():
    h = hash_password("correct horse battery staple")
    assert "correct horse" not in h
    assert h.startswith("$argon2id$")


def test_same_password_gives_different_hashes():
    assert hash_password("same-password-123") != hash_password("same-password-123")


def test_verify_accepts_correct_and_rejects_wrong():
    h = hash_password("my-long-password-1")
    assert verify_password("my-long-password-1", h) is True
    assert verify_password("wrong-password-12", h) is False


def test_verify_rejects_garbage_hash():
    assert verify_password("anything", "not-a-hash") is False


def test_fresh_hash_does_not_need_rehash():
    assert needs_rehash(hash_password("another-long-pass-1")) is False