from market import app, db
from market.models import User, Item

if __name__ == "__main__":
    # Ensure the database operations are performed within the app context
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # print("Dropped all tables from the database.")

        # Recreate all tables
        db.create_all()
        # print("Recreated all tables in the database.")

        # Add sample users
        sample_users = [
            User(username="john_doe", email_address="john@example.com", password_hash="hashed_password1"),
            User(username="jane_doe", email_address="jane@example.com", password_hash="hashed_password2"),
        ]
        db.session.bulk_save_objects(sample_users)
        db.session.commit()
        # print("Added sample users to the database.")

        # Assign items to users
        user_john = User.query.filter_by(username="john_doe").first()
        user_jane = User.query.filter_by(username="jane_doe").first()

        if user_john and user_jane:
            # Add sample items
            sample_items = [
                Item(name="Phone", price=500, barcode="5634723456", description="A smartphone with excellent features.", owner=user_john.id),
                Item(name="Laptop", price=768, barcode="3425347893", description="A high-performance laptop for work and gaming.", owner=user_jane.id),
                Item(name="Keyboard", price=167, barcode="45637846578", description="A mechanical keyboard with RGB lighting.", owner=user_john.id),
            ]
            db.session.bulk_save_objects(sample_items)
            db.session.commit()
            # print("Added sample items to the database and assigned them to users.")

        # Verify the relationships
        all_users = User.query.all()
    # Run the app
    app.run(debug=True)
