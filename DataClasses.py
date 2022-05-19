import dataclasses
from dataclasses import dataclass

@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    traning_type: str
    duration: float
    distance: float
    avg_speed: float
    calories: float

    def get_message(self) -> str:
        message = '''Тип тренировки: {traning_type};\nДлительность: {duration:.3f} ч.; \
        \nДистанция: {distance:.3f} км; \nСр. скорость: {avg_speed:.3f} км/ч; \
        \nПотрачено ккал: {calories:.3f}.\n'''
        
        ss = dataclasses.asdict(self)
        return ss

a = InfoMessage('www',12,13,14,15)
sss = dataclasses.asdict(a)
print (sss)
print(a.get_message())
