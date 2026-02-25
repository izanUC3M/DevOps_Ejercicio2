import csv
from typing import Iterable

from domain import PodcastRecord, Repository


class CSVRepository(Repository):
	def __init__(self, file_path: str):
		self.file_path = file_path

	def read_all(self) -> Iterable[PodcastRecord]:
		with open(self.file_path, mode='r', encoding='utf-8') as f:
			for row in csv.DictReader(f):
				yield PodcastRecord(
					id=row.get('id', '') or '',
					user_agent=row.get('user_agent', ''),
					method=row.get('method', ''),
					uri_episode=row.get('uri_episode', ''),
				)

	def save_observation(self, observation: PodcastRecord) -> None:
		# Aquí podríamos insertar en BD (Mongo/SQL). Por ahora simulamos.
		print(f"Salvando observación: {observation.id}")
