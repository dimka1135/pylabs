#Функциональный подход
Импорт библиотеки configparser
Обяъвление словаря: conf
Объявление функции conf_read с аргументом (file):
    with open(file) as f:
        f.read()

Объявление функции conf_write с аргументом (file):
    with open(file, 'w') as f:
        f.write()


#Объектно-ориентированный подход
Импорт библиотеки configparser
Объявление класса SingletonMeta с атрибутом type: #создание шаблона
    Объявление словаря: conf
    Объявление функции __call__ c аргументами (self, *args, **kwargs):
        Если self нет в self.conf:
            то self.conf(self) = super.__call__(*args, **kwargs)
        Возвращаем self.conf(self)

Объявление класса Config с атрибутом (metaclass = SingletonMeta):
    __slots__ = ('config', )
    Объявление функции __init__ с аргументом (self):
        self.config = ConfigParser()
    Объявление функции получения атрибута (__getattribute__) с аргументами (self, name):
        try:
            Возвращаем super().__getattribute__(name)
        except AttributeError:
            Возвращаем getattr(self.config, name)

testconf = Config()
testconf.add_section("Settings")
testconf.set("Settings", "font", "Courier")
testconf.set("Settings", "font_size", "10")

font = testconf.get("Settings", "font")
font_size = testconf.get("Settings", "font_size")