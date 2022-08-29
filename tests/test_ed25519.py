from aleph_pytezos.crypto.key import Key


def test_derive_public_key_from_encoded():
    encoded_key = "edpkvUuhtQDPA9KfC3BY7ydh89hT34KTANMfX7L22BUrA9aGWg6QxF"
    key = Key.from_encoded_key(encoded_key)
    public_key_hash = key.public_key_hash()

    print(public_key_hash)

    signature = "siggLSTX5i9ZZJHb6vUoi5gNxWEjEcBD62Jjs8JdFgDND3uc9xb5YC9bUFLpBAoudhdTRNfmV7GTnJzoWUm9y1cDh7T6KX59"
    buffer = b"TEZOS\ntz1SmGHzna3YhKropa3WudVq72jhTPDBn4r5\nPOST\n41de1a7766c7e5fad54772470eefde63b6bef8683c4159d9179d74955009deb4"
    key.verify(signature, buffer)
