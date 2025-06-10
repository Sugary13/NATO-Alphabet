# 🔡 NATO Phonetic Alphabet Translator

Este proyecto convierte cualquier palabra que ingreses en su equivalente del alfabeto fonético de la OTAN (NATO), utilizando Python y `pandas`.

Por ejemplo:  
**Input:** `Python`  
**Output:** `['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']`

---

## 📚 ¿Qué es el alfabeto fonético de la OTAN?

Es un conjunto de palabras estandarizadas que se usan para deletrear letras de forma clara por radio o teléfono, muy útil en aviación, fuerzas armadas y comunicación clara entre hablantes.

---

## 🚀 Tecnologías utilizadas

- Python 3
- [pandas](https://pandas.pydata.org/) – para manejo de datos con CSV
- `nato_phonetic_alphabet.csv` – archivo con las letras y sus códigos fonéticos

---

## 💻 Cómo usar

1. Asegúrate de tener Python instalado.
2. Instala `pandas` si no lo tienes:

```bash
pip install pandas
```
3. Ejecuta el script:
python main.py

4. Ingresa una palabra cuando el programa lo solicite.

📁 Estructura del proyecto
.
├── main.py                         # Script principal

├── nato_phonetic_alphabet.csv     # CSV con letras y sus códigos fonéticos

└── README.md

✍️ Ejemplo de uso

Enter a word: Hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
