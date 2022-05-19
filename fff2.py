from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    traning_type: str
    duration: float
    distance: float
    avg_speed: float
    calories: float

    def get_message(self) -> str:
        message = 'Тип тренировки: {traning_type};\nДлительность: {duration:.3f} ч.; \
        \nДистанция: {distance:.3f} км; \nСр. скорость: {avg_speed:.3f} км/ч; \
        \nПотрачено ккал: {calories:.3f}.\n'
        return (message.format(**asdict(self)))


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP: float = 0.65
        self.M_IN_KM: int = 1000
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance()
        return (distance / 60)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__, self.duration,
                           self.get_distance(), self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        dur_minutes = self.duration * 60
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        avg_speed = self.get_mean_speed()
        return ((coeff_calorie_1 * avg_speed - coeff_calorie_2)
                * self.weight / self.M_IN_KM * dur_minutes)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ):
        super().__init__(action, duration, weight)
        self.height = height
    pass

    def get_spent_calories(self) -> float:
        dur_minutes = self.duration * 60
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        avg_speed = self.get_mean_speed()
        return (coeff_calorie_1 * self.weight + (avg_speed**2 // self.height)
                * coeff_calorie_2 * self.weight) * dur_minutes


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP: float = 1.38
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self):
        dur_minutes = self.duration * 60
        return self.length_pool*self.count_pool/self.M_IN_KM/dur_minutes

    def get_spent_calories(self) -> float:
        avg_speed = self.get_mean_speed()
        coeff_calorie_1: float = 1.1
        coeff_calorie_2: float = 2
        return (avg_speed + coeff_calorie_1) * coeff_calorie_2 * self.weight
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_dict: dict[str, Training] = {'SWM': Swimming, 'RUN': Running,
                                          'WLK': SportsWalking}
    if workout_type not in training_dict:
        raise Exception("Sorry, no training type available")
    else:
        return training_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info1 = training.show_training_info()
    print(info1.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
