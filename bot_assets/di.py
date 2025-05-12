from dal.interfaces.repositories.user import IUserRepository
from dal.interfaces.repositories.dorms import IDormRepository
from dal.interfaces.services.user import IUserService
from infrastructure.repositories.user import UserRepository
from infrastructure.repositories.dorms import DormRepository
from infrastructure.services.user import UserService


async def get_user_repository() -> IUserRepository:
    return UserRepository()

async def get_dorm_repository() -> IDormRepository:
    return DormRepository()

