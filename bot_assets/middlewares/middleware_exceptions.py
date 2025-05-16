from aiogram import BaseMiddleware
from loguru import logger

from .exceptions import ValidationError


class ValidationErrorMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        try:
            return await handler(event, data)
        except ValidationError as e:
            logger.exception(f"Exception in handler: {e}")
            await self.handler_validation_error(event, e, data)
        
        return False
    
    async def handler_validation_error(self, event, error: ValidationError, data):
        await event.answer(f'Ошибка: {error.message}')

        if error.state:
            state = data.get('state')
            if state and await state.get_state() != error.state:
                await state.set_state(error.state)