from datetime import datetime
from aiogram.fsm.state import State

from infrastructure.database.entities.models import Event
from bot_assets.middlewares.exceptions import ValidationError


class EventService():
    @staticmethod
    async def get_message_event(event: Event):
        message = f'\n Название: {event.name}'
        message += f'\n Описание: {event.description}'
        message += f'\n Дата: {event.datetime}'
        for k, v in event.data.items():
            message += f'\n {k}: {v}'
        return message
    
    @staticmethod
    async def validate_datetime(date: str, state: State):
        try:
            date = datetime.strptime(date.split()[0], '%Y-%m-%d').date()
            time = datetime.strptime(date.split()[1], '%H:%M').time()
            return datetime.combine(date, time)
        except:
            raise ValidationError(
                message='Неверный формат даты/времени',
                state=state)
