from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

complaint_router = Router()

class Complaint(StatesGroup):
    name = State()
    age = State()
    complaint = State()

@complaint_router.message(Command("complaint"))
async def process_name(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(Complaint.name)

@complaint_router.message(Complaint.name)
async def process_age(message: types.Message, state: FSMContext):
    await message.answer("сколько вам?")
    await state.set_state(Complaint.age)


@complaint_router.message(Complaint.age)
async def process_complaint(message: types.Message, state: FSMContext):
    await message.answer("Напишите вашу жалобу?")
    await state.set_state(Complaint.complaint)


@complaint_router.message(Complaint.complaint)
async def process_message(message: types.Message, state: FSMContext):
    await message.answer("Спасибо")
    await state.clear()