import os
import sys

# Aseguramos que el directorio `src` esté en sys.path para imports locales
sys.path.insert(0, os.path.dirname(__file__))

from infrastructure import CSVRepository
from application import PodcastService


def main():
	csv_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'data_toy.csv'))

	repo = CSVRepository(csv_path)
	service = PodcastService(repo)

	exitos, fallos = service.process_ingestion()

	print(f"\n--- Resumen de Proceso ---")
	print(f"Registros procesados: {len(exitos)}")
	print(f"Errores/Bots detectados: {len(fallos)}")


if __name__ == '__main__':
	main()
