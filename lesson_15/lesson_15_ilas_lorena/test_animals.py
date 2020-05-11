import unittest
import animals


class TestAnimal(unittest.TestCase):

    def test_animal_init(self):
        animal = 'dog'
        name = 'Toby'
        n_legs = 4
        gender = 'M'
        speech_type = 'bau'

        test_animals = animals.Animal(animal, name, n_legs, gender, speech_type)

        assert hasattr(test_animals, 'animal'), 'Class Animal is missing animal attribute'
        assert hasattr(test_animals, 'name'), 'Class Animal is missing name attribute'
        assert hasattr(test_animals, 'n_legs'), 'Class Animal is missing n_legs attribute'
        assert hasattr(test_animals, 'gender'), 'Class Animal is missing gender attribute'
        assert hasattr(test_animals, 'speech_type'), 'Class Animal is missing speech_type attribute'

    def test_check_speech(self):
        animal = 'cat'
        name = 'Luna'
        n_legs = 4
        gender = 'F'
        speech_type = 'meow'

        test_animals = animals.Animal(animal, name, n_legs, gender, speech_type)

        result = test_animals.check_speech_type()

        # self.assertEqual(result, 'It is dog!') --> faild test
        self.assertEqual(result, 'It is a cat!')

    def test_check_motility(self):
        animal = 'snake'
        name = 'Sandra'
        n_legs = 0
        gender = 'F'
        speech_type = 'hiss'

        test_animals = animals.Animal(animal, name, n_legs, gender, speech_type)

        result = test_animals.check_motility()

        self.assertTrue(result, f'{name} the {animal} has no legs so it slides')

    def test_is_rescue_dog(self):
        animal = 'dog'
        name = 'Lola'
        n_legs = 4
        gender = 'F'
        speech_type = 'bau'
        breed = 'Chihuahua'
        age = 1

        test_animals = animals.Dog(animal, name, n_legs, gender, speech_type, breed, age)

        result = test_animals.is_rescue_dog()

        self.assertTrue(result, f'{name} is a {breed} hence it is not a rescue dog')

    def test_check_age(self):
        animal = 'dog'
        name = 'Lola'
        n_legs = 4
        gender = 'F'
        speech_type = 'bau'
        breed = 'Chihuahua'
        age = 1

        test_animals = animals.Dog(animal, name, n_legs, gender, speech_type, breed, age)

        test_animals.age = age
        # self.assertIsInstance(age, float), 'Number must be a integer!'
        self.assertIsInstance(age, int)


if __name__ == '__main__':
    unittest.main()
