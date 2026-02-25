from dataclasses import dataclass
from typing import Protocol, Iterable


@dataclass
class PodcastRecord:
	id: str
	user_agent: str
	method: str
	uri_episode: str


class Repository(Protocol):
	def read_all(self) -> Iterable[PodcastRecord]:
		...

	def save_observation(self, observation: PodcastRecord) -> None:
		...
