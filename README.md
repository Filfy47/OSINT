# OSINT Tool

Инструмент для поиска информации по юзернейму в открытом интернете.

## Описание

OSINT (Open Source Intelligence) - это поиск информации в открытых источниках.
Этот инструмент помогает найти аккаунты человека в разных социальных сетях по его юзернейму.

## Установка и использование

```bash
git clone https://github.com/Filfy47/OSINT.git
cd OSINT
pip install -r requirements.txt
```
```bash
python OSINT.py --username (Юзернейм)
```
## Примеры

```bash
python OSINT.py --username john_doe
python OSINT.py --username alice
```
## Технологии

- Python 3.8+
- requests (HTTP запросы)
- argparse (CLI интерфейс)
- concurrent.futures (многопоточность)
