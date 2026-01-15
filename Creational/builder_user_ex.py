class User:
    """
    Immutable User class with required and optional fields.
    Use UserBuilder to construct instances.
    """

    def __init__(self, builder):
        """Private constructor - use UserBuilder instead."""
        # Required fields
        self._first_name = builder._first_name
        self._lastname = builder._lastname
        self._email_address = builder._email_address

        # Optional fields
        self._age = builder._age
        self._phone_number = builder._phone_number
        self._address = builder._address

    # Getters only - no setters (immutable)
    @property
    def first_name(self):
        return self._first_name

    @property
    def lastname(self):
        return self._lastname

    @property
    def age(self):
        return self._age

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def address(self):
        return self._address

    @property
    def email_address(self):
        return self._email_address

    def __str__(self):
        return (
            f"User(firstName='{self.first_name}', "
            f"lastname='{self.lastname}', "
            f"age={self.age}, "
            f"phoneNumber='{self.phone_number}', "
            f"address='{self.address}', "
            f"emailAddress='{self.email_address}')"
        )

    def __repr__(self):
        return self.__str__()


class UserBuilder:
    """
    Builder class for constructing User objects with a fluent interface.
    """

    def __init__(self):
        # Initialize all fields
        self._first_name = None
        self._lastname = None
        self._email_address = None
        self._age = None
        self._phone_number = None
        self._address = None

    def set_first_name(self, first_name):
        """Set the first name (required)."""
        self._first_name = first_name
        return self  # Return self for method chaining

    def set_lastname(self, lastname):
        """Set the last name (required)."""
        self._lastname = lastname
        return self

    def set_email_address(self, email_address):
        """Set the email address (required)."""
        self._email_address = email_address
        return self

    def set_age(self, age):
        """Set the age (optional)."""
        self._age = age
        return self

    def set_phone_number(self, phone_number):
        """Set the phone number (optional)."""
        self._phone_number = phone_number
        return self

    def set_address(self, address):
        """Set the address (optional)."""
        self._address = address
        return self

    def build(self):
        """
        Build and return the User object.
        Validates that all required fields are set.
        """
        # Validate required fields
        if not self._first_name:
            raise ValueError("firstName is required")
        if not self._lastname:
            raise ValueError("lastname is required")
        if not self._email_address:
            raise ValueError("emailAddress is required")

        # Create and return the User object
        return User(self)


# Example usage
if __name__ == "__main__":
    print("=== Example 1: User with all fields ===")
    user1 = (
        UserBuilder()
        .set_first_name("John")
        .set_lastname("Doe")
        .set_email_address("john.doe@example.com")
        .set_age(30)
        .set_phone_number("+1-555-1234")
        .set_address("123 Main St, New York, NY")
        .build()
    )

    print(user1)
    print(f"First Name: {user1.first_name}")
    print(f"Email: {user1.email_address}")

    print("\n=== Example 2: User with only required fields ===")
    user2 = (
        UserBuilder()
        .set_first_name("Jane")
        .set_lastname("Smith")
        .set_email_address("jane.smith@example.com")
        .build()
    )

    print(user2)

    print("\n=== Example 3: User with some optional fields ===")
    user3 = (
        UserBuilder()
        .set_first_name("Bob")
        .set_lastname("Johnson")
        .set_email_address("bob.j@example.com")
        .set_age(25)
        .set_phone_number("+1-555-5678")
        .build()
    )

    print(user3)

    print("\n=== Example 4: Testing immutability ===")
    print("Attempting to modify user1.first_name...")
    try:
        user1.first_name = "Modified"  # This will fail
    except AttributeError as e:
        print(f"✓ Immutability enforced: {e}")

    print("\n=== Example 5: Testing validation (missing required field) ===")
    try:
        invalid_user = (
            UserBuilder().set_first_name("Test").build()
        )  # Missing lastname and email
    except ValueError as e:
        print(f"✓ Validation works: {e}")
