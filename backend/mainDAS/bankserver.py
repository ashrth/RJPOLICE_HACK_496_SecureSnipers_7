import random
from rest_framework.views import APIView
import requests
from rest_framework.response import Response



class BankServerView(APIView):
    backend_url = 'http://127.0.0.1:8000/api/process-real-time-transactions'

    def generate_dummy_transaction(self):
        return {
        'account_number': f'123456789{random.randint(1000, 9999)}',
        'available_credit': round(random.uniform(100.0, 5000.0), 2),
        'amount': round(random.uniform(10.0, 1000.0), 2),
        'transaction_category': random.choice(['LX', 'auto', 'internet', 'recrea', 'entertainment', 'gas', 'fashion', 'international', 'health', 'electronic', 'gift card', 'deal', 'apparel', 'fastfood']),
        'day': random.randint(1, 31),
        'time': f'{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}',
        'payment_failed': random.choice([True, False]),
        'forget_password': random.choice([True, False]),
        'KYC_incomplete': random.choice([True, False]),
        'multiple_accounts': random.randint(1, 4),
    }


    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            dummy_transactions = [self.generate_dummy_transaction() for _ in range(10)]
            for transaction in dummy_transactions:
                try:

                    response = requests.post(self.backend_url, data=transaction)

                except Exception as e:
                    print(f"Error processing dummy transaction: {str(e)}")

            return Response({'message': 'Transaction sent successfully', 'response': response.text})

        return Response({'error': 'Invalid request method'})

