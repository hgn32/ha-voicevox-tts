from __future__ import annotations

import logging

import aiohttp
from homeassistant.components.tts import TextToSpeechEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([VoicevoxTTSEntity(hass, config_entry)])


class VoicevoxTTSEntity(TextToSpeechEntity):
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        self._hass = hass
        self._host: str = config_entry.data["host"]
        self._port: int = config_entry.data["port"]
        self._speaker: int = config_entry.data.get("speaker", 10)
        self._attr_unique_id = f"{DOMAIN}_{self._host}_{self._port}"
        self._attr_name = f"VOICEVOX TTS ({self._host}:{self._port})"

    @property
    def should_poll(self) -> bool:
        return False

    @property
    def supported_languages(self) -> list[str]:
        return ["ja"]

    @property
    def default_language(self) -> str:
        return "ja"

    @property
    def supported_options(self) -> list[str]:
        return ["speaker"]

    async def async_get_tts_audio(
        self, message: str, language: str, options: dict | None = None
    ) -> tuple[str | None, bytes | None]:
        speaker = (options or {}).get("speaker", self._speaker)
        base = f"http://{self._host}:{self._port}"
        session = async_get_clientsession(self._hass)
        try:
            async with session.post(
                f"{base}/audio_query",
                params={"text": message, "speaker": speaker},
            ) as resp:
                if resp.status != 200:
                    _LOGGER.error("audio_query failed: status=%s", resp.status)
                    return None, None
                query = await resp.json()

            async with session.post(
                f"{base}/synthesis",
                params={"speaker": speaker, "enable_interrogative_upspeak": "true"},
                json=query,
            ) as resp:
                if resp.status != 200:
                    _LOGGER.error("synthesis failed: status=%s", resp.status)
                    return None, None
                audio = await resp.read()

        except aiohttp.ClientError as exc:
            _LOGGER.error("VOICEVOX API error: %r", exc)
            return None, None

        return "wav", audio
