from typing import List, Tuple
import uuid

from domain import PodcastRecord, Repository


class PodcastService:
	"""Contiene las reglas de validación y lógica de negocio."""
	def __init__(self, repository: Repository):
		self.repository = repository
		self.bot_keywords = ["BOT", "SPIDER", "CRAWLER", "HERITRIX"]

	def process_ingestion(self) -> Tuple[List[PodcastRecord], List[dict]]:
		processed_records: List[PodcastRecord] = []
		errors: List[dict] = []

		for record in self.repository.read_all():
			is_bot = any(k in (record.user_agent or "").upper() for k in self.bot_keywords)
			is_valid_method = (record.method or "") == "GET"

			if not is_bot and is_valid_method:
				processed_records.append(record)
				self.repository.save_observation(record)
			else:
				reason = "Bot detected" if is_bot else "Bad method"
				errors.append({"id": str(uuid.uuid4()), "metrica": reason, "uri": record.uri_episode})

		return processed_records, errors
