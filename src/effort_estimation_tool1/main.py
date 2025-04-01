#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from .crew import EffortEstimationTool

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'sow': """Here is the Statement of Work for the Porter project: [2:54 PM, 7/13/2023] Harsha S Prakash: Video #4 Porter kind of application to be designed and developed




Functional Requirements

User Registration: The app should allow users to register by providing their basic information such as name, contact details, and address.
Driver and Customer


Login and Authentication: The app should provide a secure login system with authentication to ensure that only registered users can access the app's features.

Driver and Customer and Admin

Profile Creation: Users should be able to create and manage their profiles, including adding and updating personal information, contact details, and delivery preferences.

Driver and Customer

Booking Service: The app should allow users to request the transportation of goods from one place to another by providing relevant details such as pickup and delivery locations, package size and weight, and any specific requirements.

Customer

Service Availability and Scheduling: The app should provide users with real-time information on the availability of porter services, including the estimated wait time and the ability to schedule pickups and deliveries at convenient times.

Customer

Tracking and Notifications: Users should be able to track the progress of their delivery in real-time and receive notifications about the status updates, including pickup confirmation, estimated time of arrival, and delivery completion.

Driver and Customer

Payment Integration: The app should integrate a secure payment system to facilitate seamless transactions between users and service providers, supporting multiple payment options such as credit/debit cards, digital wallets, and cash on delivery.

Driver and CUstomer

Service Provider Management: The app should have a system for onboarding and managing service providers (porters), including verifying their credentials, tracking their availability, and assigning them to specific delivery requests.

Admin

Ratings and Reviews: Users should be able to rate and provide feedback on the quality of service received, allowing for a transparent and reliable rating system to help other users make informed decisions.

Customers and Drivers

[2:54 PM, 7/13/2023] Harsha S Prakash: 

User Registration and Authentication:
        Customers and drivers should be able to register and create their accounts.
        The app should support secure authentication methods to ensure the privacy and security of user data.

Driver and Customer

    User Roles and Dashboards:
        The app should have separate interfaces for customers and drivers, each with their own dashboards.

General

        Customers should be able to book vehicles, track their shipments, and manage their bookings.

Customer

        Drivers should be able to view and accept/reject booking requests, manage their availability, and track their assigned shipments.

Drivers


    Vehicle Selection:
        Customers should be able to choose from a list of available vehicles based on their capacity.

Customer

        The app should display the capacity, type, and other relevant information about each vehicle to help customers make informed decisions.

Customer

    Booking Process:
        Customers should be able to enter pickup and delivery locations, along with any intermediate stops if required.

Customer

        The app should calculate and display the estimated cost and time for the shipment.

Customer


        Customers should be able to schedule a pickup time and date based on their requirements.

Customer

    Real-time Tracking:
        Customers should be able to track the location of their shipment in real-time.

Customer


        Drivers should have access to navigation features to efficiently reach pickup and delivery locations.

Driver


    Notifications and Alerts:
        Both customers and drivers should receive notifications and alerts regarding booking confirmations, updates, delays, or cancellations.

Driver and Customer

        Notifications can be sent via email, SMS, or in-app push notifications, based on user preferences.

General

    Payment Integration:
        The app should support secure payment options to facilitate transactions between customers and drivers.

Driver and Customer

        Multiple payment methods such as credit/debit cards, digital wallets, or cash on delivery should be supported.

Customer and Driver

    Rating and Review System:
        Customers should be able to rate and provide feedback on the driver and the overall service.

Customer and Driver

        Drivers should also have the ability to rate and review customers based on their experience.

Drriver

    Driver Availability and Acceptance:
        Drivers should have the option to set their availability status (online/offline) for accepting booking requests.

        The app should notify drivers about nearby booking requests, allowing them to accept or reject based on their availability.





    Admin Dashboard:
        An administrative interface should be available to manage and monitor the overall system.
        Admins should be able to view and manage user accounts, vehicles, bookings, and resolve any conflicts or issues. - TIcketing

    Support and Help Center:
        The app should provide a support center or help desk where users can get assistance or report any issues they encounter.


        Contact information and FAQs should be easily accessible within the app.

    Localization and Internationalization:
        The app should support multiple languages and currencies to cater to a diverse user base.

        Users should be able to switch between different languages and view prices in their preferred currency.
Customer and Driver




[2:54 PM, 7/13/2023] Harsha S Prakash: User Profile Management:
        Users should be able to create and manage their profiles, including personal information, contact details, and preferences.
Genral

        The app should allow users to update their profiles and view their booking history.


    Advanced Search and Filtering:
        Customers should be able to search for available vehicles based on specific criteria such as vehicle type, capacity, price range, or availability.

        The app should provide advanced filtering options to narrow down search results and help customers find the most suitable vehicle.
General

    Multiple Booking Options:
        Customers should have the flexibility to make different types of bookings, such as immediate or scheduled pickups, recurring bookings, or pre-booking for future dates.
        The app should allow customers to modify or cancel their bookings within a specified time frame.

    Multi-Stop Routing:
        The app should support the inclusion of multiple stops or waypoints between the pickup and delivery locations.
        Customers should be able to add, remove, or rearrange stops as needed during the booking process.

    Distance Calculation and Fare Estimation:
        The app should calculate the distance between pickup and delivery locations, considering the chosen route and any intermediate stops.
        Based on the distance and the selected vehicle, the app should provide an accurate fare estimation for the shipment.

    Ratings and Reviews Aggregation:
        The app should aggregate and display average ratings and reviews for drivers and vehicles to help customers make informed decisions.
        Ratings and reviews can be used to rank drivers or vehicles based on their performance and reliability.

    Order History and Invoices:
        Customers should have access to their order history, including past bookings, details of shipped goods, and corresponding invoices.
        Invoices should include relevant information such as pickup and delivery dates, distance traveled, fare breakdown, and payment details.
Genral

    Driver Navigation and Routing:
        The app should provide drivers with efficient navigation routes to reach pickup and delivery locations, considering real-time traffic information.
        Drivers should have the ability to view turn-by-turn directions and receive voice-guided navigation instructions.

    Driver Earnings and Payouts:
        The app should track and calculate driver earnings based on completed shipments, distance traveled, and applicable fare rates.
        Drivers should have access to their earnings history and be able to request payouts or withdrawals through the app.
Drivers

    Customer Support Integration:
        The app should integrate with customer support systems, allowing users to initiate support requests directly from the app.
        Support tickets should be logged, tracked, and resolved by the customer support team efficiently.

    Driver Background Checks and Verification:
        The app should incorporate a process for driver background checks and verification to ensure the safety and reliability of the service.
        Drivers should provide necessary documentation and undergo verification procedures before being allowed to accept bookings.
Research for Docs needed

    Dynamic Pricing and Surge Pricing:
        The app should support dynamic pricing based on factors such as demand, distance, time of day, or special events.
        Surge pricing can be implemented during peak demand periods to incentivize more drivers to be available.

    Integration with External APIs:
        The app may integrate with external APIs for services such as geolocation, mapping, payment gateways, or SMS notifications to enhance functionality and user experience.
Email, Push Notifications, Chat
.""",
'historical_data': 'Example: Secure Login System - Effort: 5 days, Buffer: 1 day, Testing: 2 days, Risk: Low, Confidence: 4'
    }
    
    try:
        EffortEstimationTool().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        EffortEstimationTool().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        EffortEstimationTool().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        EffortEstimationTool().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
