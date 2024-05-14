from collections import namedtuple
from datetime import datetime, timedelta
from enum import StrEnum
import re
from typing import Any, List, Optional

from datetimerange import DateTimeRange
from pydantic import GetCoreSchemaHandler, field_validator, HttpUrl
from pydantic_core import CoreSchema, core_schema
from pydantic_xml import attr, BaseXmlModel, element, wrapped


class NationCategory(StrEnum):
    PSYCHOTIC_DICTATORSHIP = "Psychotic Dictatorship"
    CORRUPT_DICTATORSHIP = "Corrupt Dictatorship"
    IRON_FIST_SOCIALISTS = "Iron Fist Socialists"
    IRON_FIST_CONSUMERISTS = "Iron Fist Consumerists"
    FATHER_KNOWS_BEST_STATE = "Father Knows Best State"
    MOTHER_KNOWS_BEST_STATE = "Mother Knows Best State"
    LIBERTARIAN_POLICE_STATE = "Libertarian Police State"
    CORPORATE_POLICE_STATE = "Corporate Police State"
    COMPULSORY_CONSUMERIST_STATE = "Compulsory Consumerist State"
    BENEVOLENT_DICTATORSHIP = "Benevolent Dictatorship"
    AUTHORITARIAN_DEMOCRACY = "Authoritarian Democracy"
    DEMOCRATIC_SOCIALISTS = "Democratic Socialists"
    SCANDINAVIAN_LIBERAL_PARADISE = "Scandinavian Liberal Paradise"
    MORALISTIC_DEMOCRACY = "Moralistic Democracy"
    INOFFENSIVE_CENTRIST_DEMOCRACY = "Inoffensive Centrist Democracy"
    LEFT_LEANING_COLLEGE_STATE = "Left-Leaning College State"
    RIGHT_WING_UTOPIA = "Right-Wing Utopia"
    CAPITALIST_PARADISE = "Capitalist Paradise"
    CAPITALIZT = "Capitalizt"
    TYRANNY_BY_MAJORITY = "Tyranny by Majority"
    LIBERAL_DEMOCRATIC_SOCIALISTS = "Liberal Democratic Socialists"
    LEFT_WING_UTOPIA = "Left-Wing Utopia"
    CONSERVATIVE_DEMOCRACY = "Conservative Democracy"
    NEW_YORK_TIMES_DEMOCRACY = "New York Times Democracy"
    CIVIL_RIGHTS_LOVEFEST = "Civil Rights Lovefest"
    FREE_MARKET_PARADISE = "Free Market Paradise"
    CORPORATE_BORDELLO = "Corporate Bordello"
    ANARCHY = "Anarchy"


class WAStatus(StrEnum):
    NON_MEMBER = "Non-member"
    MEMBER = "WA Member"
    DELEGATE = "WA Delegate"


class WAVote(StrEnum):
    UNDECIDED = "UNDECIDED"
    FOR = "FOR"
    AGAINST = "AGAINST"


class MajorIndustry(StrEnum):
    ARMS_MANUFACTURING = "Arms Manufacturing"
    AUTOMOBILE_MANUFACTURING = "Automobile Manufacturing"
    BASKEST_WEAVING = "Basket Weaving"
    BEVERAGE_SALES = "Beverage Sales"
    BOOK_PUBLISHING = "Book Publishing"
    CHEESE_EXPORTS = "Cheese Exports"
    FURNITURE_RESTORATION = "Furniture Restoration"
    GAMBLING = "Gambling"
    INFORMATION_TECHNOLOGY = "Information Technology"
    INSURANCE = "Insurance"
    MINING = "Mining"
    PIZZA_DELIVERY = "Pizza Delivery"
    RETAIL = "Retail"
    TIMBER_WOODCHIPPING = "Timber Woodchipping"
    TROUT_FISHING = "Trout Fishing"


class GovernmentBudget(BaseXmlModel, tag="GOVT"):
    administration: float = element(tag="ADMINISTRATION")
    defence: float = element(tag="DEFENCE")
    education: float = element(tag="EDUCATION")
    environment: float = element(tag="ENVIRONMENT")
    healthcare: float = element(tag="HEALTHCARE")
    commerce: float = element(tag="COMMERCE")
    international_aid: float = element(tag="INTERNATIONALAID")
    law_and_order: float = element(tag="LAWANDORDER")
    public_transport: float = element(tag="PUBLICTRANSPORT")
    social_equality: float = element(tag="SOCIALEQUALITY")
    spirituality: float = element(tag="SPIRITUALITY")
    welfare: float = element(tag="WELFARE")

    @property
    def defense(self):
        return self.defence


class GovernmentPriority(StrEnum):
    ADMINISTRATION = "Administration"
    DEFENCE = "Defence"
    EDUCATION = "Education"
    ENVIRONMENT = "Environment"
    HEALTHCARE = "Healthcare"
    COMMERCE = "Commerce"
    INTERNATIONAL_AID = "International Aid"
    LAW_AND_ORDER = "Law and Order"
    PUBLIC_TRANSPORT = "Public Transport"
    SOCIALEQUALITY = "Social Equality"
    SPIRITUALITY = "Spirituality"
    WELFARE = "Welfare"


class InfluenceRank(StrEnum):
    ZERO = "Zero"
    UNPROVEN = "Unproven"
    HATCHLING = "Hatchling"
    NEWCOMER = "Newcomer"
    NIPPER = "Nipper"
    MINNOW = "Minnow"
    SPRAT = "Sprat"
    SHOESHINER = "Shoeshiner"
    PAGE = "Page"
    SQUIRE = "Squire"
    APPRENTICE = "Apprentice"
    VASSAL = "Vassal"
    TRUCKLER = "Truckler"
    HANDSHAKER = "Handshaker"
    DUCKSPEAKER = "Duckspeaker"
    ENVOY = "Envoy"
    DIPLOMAT = "Diplomat"
    AMBASSADOR = "Ambassador"
    AUXILIARY = "Auxiliary"
    NEGOTIATOR = "Negotiator"
    CONTENDER = "Contender"
    INSTIGATOR = "Instigator"
    DEALMAKER = "Dealmaker"
    ENFORCER = "Enforcer"
    EMINENCE_GRISE = "Eminence Grise"
    POWERBROKER = "Powerbroker"
    POWER = "Power"
    SUPERPOWER = "Superpower"
    DOMINATOR = "Dominator"
    HEGEMONY = "Hegemony"
    HERMIT = "Hermit"

    def _index(self):
        return list(InfluenceRank).index(self)
    
    def __lt__(self, other):
        if type(other) is InfluenceRank:
            return self._index() < other._index()
        return NotImplemented

    def __le__(self, other):
        if type(other) is InfluenceRank:
            return self._index() <= other._index()
        return NotImplemented

    def __gt__(self, other):
        if type(other) is InfluenceRank:
            return self._index() > other._index()
        return NotImplemented

    def __ge__(self, other):
        if type(other) is InfluenceRank:
            return self._index >= other._index()
        return NotImplemented


class CauseOfDeath(StrEnum):
    OLD_AGE = "Old Age"
    HEART_DISEASE = "Heart Disease"
    MURDER = "Murder"
    LOST_IN_WILDERNESS = "Lost in Wilderness"
    ACTS_OF_GOD = "Acts of God"
    CANCER = "Cancer"
    EXPOSURE = "Exposure"
    SUICIDE_WHILE_IN_POLICE_CUSTODY = "Suicide While in Police Custody"
    ACCIDENT = "Accident"
    ANIMAL_ATTACK = "Animal Attack"
    DISAPPEARANCE = "Disappearance"
    WORK = "Work"
    RITUAL_SACRIFICE = "Ritual Sacrifice"
    WAR = "War"
    CAPITAL_PUNISHMENT = "Capital Punishment"
    BUNGEE_JUMPING = "Bungee Jumping"
    SCURVY = "Scurvy"
    NUCLEAR_SPILL = "Nuclear Spill"
    INVOLUNTARY_EUTHANASIA = "Involuntary Euthanasia"
    SUNBURN = "Sunburn"
    VAT_LEAKAGE = "Vat Leakage"
    MALNOURISHMENT = "Malnourishment"
    SPACE_SHUTTLE_MISHAP = "Space Shuttle Mishap"


class DeathPercentage(BaseXmlModel, tag="CAUSE"):
    type: CauseOfDeath = attr(name="type")
    percentage: float


class Sectors(BaseXmlModel, tag="SECTORS"):
    black_market: float = element(tag="BLACKMARKET")
    government: float = element(tag="GOVERNMENT")
    industry: float = element(tag="INDUSTRY")
    public: float = element(tag="PUBLIC")


class Nation(BaseXmlModel, tag="NATION", search_mode="unordered"):
    name: Optional[str] = element(tag="NAME", default=None)
    dbid: Optional[int] = element(tag="DBID", default=None)
    type: Optional[str] = element(tag="TYPE", default=None)
    motto: Optional[str] = element(tag="MOTTO", default=None)
    category: Optional[NationCategory] = element(tag="CATEGORY", default=None)
    wa_status: Optional[WAStatus] = element(tag="UNSTATUS", default=None)
    endorsements: Optional[str] = element(tag="ENDORSEMENTS", default=None)
    ga_vote: Optional[WAVote] = element(tag="GAVOTE", default=None)
    sc_vote: Optional[WAVote] = element(tag="SCVOTE", default=None)
    issues_answered: Optional[int] = element(tag="ISSUES_ANSWERED", default=None)
    # freedom
    region: Optional[str] = element(tag="REGION", default=None)
    population: Optional[int] = element(tag="POPULATION", default=None)
    tax: Optional[float] = element(tag="TAX", default=None)
    animal: Optional[str] = element(tag="ANIMAL", default=None)
    animal_trait: Optional[str] = element(tag="ANIMALTRAIT", default=None)
    currency: Optional[str] = element(tag="CURRENCY", default=None)
    flag: Optional[HttpUrl] = element(tag="FLAG", default=None)
    demonym_adjective: Optional[str] = element(tag="DEMONYM", default=None)
    demonym: Optional[str] = element(tag="DEMONYM2", default=None)
    demonym_plural: Optional[str] = element(tag="DEMONYM2PLURAL", default=None)
    gdp: Optional[int] = element(tag="GDP", default=None)
    income: Optional[int] = element(tag="INCOME", default=None)
    richest: Optional[int] = element(tag="RICHEST", default=None)
    poorest: Optional[int] = element(tag="POOREST", default=None)
    major_industry: Optional[MajorIndustry] = element(tag="MAJORINDUSTRY", default=None)
    crime: Optional[str] = element(tag="CRIME", default=None)
    sensibilities: Optional[str] = element(tag="SENSIBILITIES", default=None)
    goverment_priority: Optional[GovernmentPriority] = element(tag="GOVTPRIORITY", default=None)
    budget: Optional[GovernmentBudget] = element(tag="GOVT", default=None)
    first_login: Optional[datetime] = element(tag="FIRSTLOGIN", default=None)
    last_login: Optional[datetime] = element(tag="LASTLOGIN", default=None)
    last_activity: Optional[str] = element(tag="LASTACTIVITY", default=None)
    influence: Optional[InfluenceRank] = element(tag="INFLUENCE", default=None)
    # freedom scores
    public_sector: Optional[float] = element(tag="PUBLICSECTOR", default=None)
    deaths: Optional[List[DeathPercentage]] = wrapped("DEATHS", element(tag="CAUSE", default=None))
    leader: Optional[str] = element(tag="LEADER", default=None)
    capital: Optional[str] = element(tag="CAPITAL", default=None)
    religion: Optional[str] = element(tag="RELIGION", default=None)
    factbooks: Optional[int] = element(tag="FACTBOOKS", default=None)
    dispatches: Optional[int] = element(tag="DISPATCHES", default=None)
    sectors: Optional[Sectors] = element(tag="SECTORS", default=None)

    @field_validator("endorsements")
    @classmethod
    def deserialize_endorsements(cls, raw: Optional[str]) -> Optional[List[str]]:
        return raw if raw is None else raw.split(",")

    @field_validator("population")
    @classmethod
    def deserialize_population(cls, raw: Optional[int]) -> Optional[int]:
        return raw if raw is None else raw * 1000000

    @field_validator("sensibilities")
    @classmethod
    def deserialize_sensibilities(cls, raw: Optional[int]) -> Optional[List[str]]:
        return raw if raw is None else raw.split(", ")

    @field_validator("last_activity")
    @classmethod
    def deserialize_last_activity(cls, raw: Optional[str]) -> Optional[DateTimeRange]:
        if raw is None:
            return raw
        match = re.search(r"(?:(\d+) (minute|hour|day)s?|(Seconds)) ago", raw)
        if match is None:
            return raw
        now = datetime.now()
        if match.group(3) is not None:
            return DateTimeRange(now - timedelta(minutes=1), now)
        else:
            unit, val = match.group(2), int(match.group(1))
            return DateTimeRange(
                now - timedelta(**{f"{unit}s": val + 1}),
                now - timedelta(**{f"{unit}s": val})
            )

    @field_validator("influence")
    @classmethod
    def deserialize_influence(cls, raw: Optional[str]) -> Optional[InfluenceRank]:
        return raw if raw is None else InfluenceRank(raw)


class Authority:
    executive: bool
    world_assembly: bool
    appearance: bool
    border_control: bool
    communications: bool
    embassies: bool
    polls: bool

    def __init__(self, raw: str):
        flags = set(raw)
        self.executive = "X" in flags
        self.world_assembly = "W" in flags
        self.appearance = "A" in flags
        self.border_control = "B" in flags
        self.communications = "C" in flags
        self.embassies = "E" in flags
        self.polls = "P" in flags


class Region(BaseXmlModel, tag="REGION", search_mode="unordered"):
    name: Optional[str] = element(tag="NAME", default=None)
    dbid: Optional[int] = element(tag="DBID", default=None)
    last_update: Optional[datetime] = element(tag="LASTUPDATE", default=None)
    last_major_update: Optional[datetime] = element(tag="LASTMAJORUPDATE", default=None)
    last_minor_update: Optional[datetime] = element(tag="LASTMINORUPDATE", default=None)
    factbook: Optional[str] = element(tag="FACTBOOK", default=None)
    dispatches: Optional[str] = element(tag="DISPATCHES", default=None)
    num_nations: Optional[int] = element(tag="NUMNATIONS", default=None)
    nations: Optional[str] = element(tag="NATIONS", default=None)
    wa_nations: Optional[str] = element(tag="UNNATIONS", default=None)
    delegate: Optional[str] = element(tag="DELEGATE", default=None)
    delegate_authority: Optional[str] = element(tag="DELEGATEAUTH", default=None)

    @field_validator("dispatches")
    @classmethod
    def deserialize_dispatches(cls, raw: Optional[str]) -> Optional[List[int]]:
        return raw if raw is None else [int(x) for x in raw.split(",")]

    @field_validator("nations")
    @classmethod
    def deserialize_nations(cls, raw: Optional[str]) -> Optional[List[str]]:
        return raw if raw is None else raw.split(":")

    @field_validator("wa_nations")
    @classmethod
    def deserialize_wa_nations(cls, raw: Optional[str]) -> Optional[List[str]]:
        return raw if raw is None else raw.split(",")

    @field_validator("delegate_authority")
    @classmethod
    def deserialize_delegate_authority(cls, raw: Optional[str]) -> Optional[Authority]:
        return raw if raw is None else Authority(raw)
