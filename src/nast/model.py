from collections import namedtuple
from datetime import datetime, timedelta
from enum import StrEnum
import re
from typing import List, Optional

from pydantic import field_validator
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


LastActivityRange = namedtuple("LastActivityRange", ["start", "end"])


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


class Nation(BaseXmlModel, tag="NATION", search_mode="unordered"):
    name: Optional[str] = element(tag="NAME", default=None)
    dbid: Optional[int] = element(tag="DBID", default=None)
    type: Optional[str] = element(tag="TYPE", default=None)
    motto: Optional[str] = element(tag="MOTTO", default=None)
    category: Optional[NationCategory] = element(tag="CATEGORY", default=None)
    wa_status: Optional[WAStatus] = element(tag="UNSTATUS", default=None)
    endorsements: Optional[List[str]] = element(tag="ENDORSEMENTS", default=None)
    ga_vote: Optional[WAVote] = element(tag="GAVOTE", default=None)
    sc_vote: Optional[WAVote] = element(tag="SCVOTE", default=None)
    issues_answered: Optional[int] = element(tag="ISSUES_ANSWERED", default=None)
    # freedom
    region: Optional[str] = element(tag="REGION", default=None)
    population: Optional[int] = element(tag="POPULATION", default=None)
    tax: Optional[float] = element(tag="TAX", default=None)
    animal: Optional[str] = element(tag="ANIMAL", default=None)
    currency: Optional[str] = element(tag="CURRENCY", default=None)
    flag: Optional[str] = element(tag="FLAG", default=None)
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
    goverment_priority: Optional[GovernmentPriority] = element(tag="GOVERNMENTPRIORITY", default=None)
    budget: Optional[GovernmentBudget] = element(tag="GOVT", default=None)
    first_login: Optional[datetime] = element(tag="FIRSTLOGIN", default=None)
    last_login: Optional[datetime] = element(tag="LASTLOGIN", default=None)
    # last_activity: Optional[LastActivityRange] = element(tag="LASTACTIVITY", default=None)
    influence: Optional[InfluenceRank] = element(tag="INFLUENCE", default=None)
    # freedom scores
    public_sector: Optional[float] = element(tag="PUBLICSECTOR", default=None)
    deaths: List[DeathPercentage] = wrapped("DEATHS", element(tag="CAUSE"))
    lead: Optional[str] = element(tag="LEADER", default=None)
    capital: Optional[str] = element(tag="CAPITAL", default=None)
    religion: Optional[str] = element(tag="RELIGION", default=None)
    factbooks: Optional[int] = element(tag="FACTBOOKS", default=None)
    dispatches: Optional[int] = element(tag="DISPATCHES", default=None)

    @field_validator("endorsements", mode="before")
    @classmethod
    def validate_endorsements(cls, raw):
        return raw[0].split(",") if raw else []

    @field_validator("population", mode="before")
    @classmethod
    def validate_population(cls, raw):
        return int(raw) * 1000000

    #@field_validator("last_activity", mode="before")
    @classmethod
    def validate_last_activity(cls, raw):
        match = re.search(r"(?:(\d+) (minute|hour|day)s?|(Seconds)) ago", raw)
        if match is None:
            return
        now = datetime.now()
        if match.group(3) is not None:
            return LastActivityRange(now - timedelta(minutes=1), now)
        else:
            return LastActivityRange(
                now - timedelta(**{f"{match.group(2)}s": int(match.group(1)) + 1}),
                now - timedelta(**{f"{match.group(2)}s": int(match.group(1))})
            )

    @field_validator("influence", mode="before")
    @classmethod
    def validate_influence(cls, raw):
        return InfluenceRank(raw)
