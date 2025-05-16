import shared.logging  # initialize logging
from app.interfaces.cli_controller import CLIController
from app.services.number_service import NumberService
from app.services.voice_service import VoiceService
from app.services.messaging_service import MessagingService
from app.services.account_service import AccountService


def main():
    number_service = NumberService()
    voice_service = VoiceService()
    messaging_service = MessagingService()
    account_service = AccountService()

    controller = CLIController(
        number_service=number_service,
        voice_service=voice_service,
        messaging_service=messaging_service,
        account_service=account_service
    )
    controller.run()

if __name__ == "__main__":
    main()
