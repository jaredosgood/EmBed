import uuid

def create_guid():
    """
    Generates a GUID (Globally Unique Identifier).

    Returns:
    - A string representation of the generated GUID.
    """
    return str(uuid.uuid4())

# # Example usage
# guid = create_guid()
# print(guid)