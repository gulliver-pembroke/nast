from os import path
from unittest.mock import patch

from nast.model import GovernmentPriority, MajorIndustry, Nation, NationCategory, WAStatus, WAVote


def test_nation_shards():
    filename = path.join(path.dirname(__file__), "data/nations/testlandia.xml")
    with open(filename, encoding="utf8") as file:
        xml = file.read()
    nation = Nation.from_xml(xml)

    assert nation.name == "Testlandia"
    assert nation.dbid == 1
    assert nation.type == "Hive Mind"
    assert nation.motto == "Fixed, thanks."
    assert nation.category == NationCategory.INOFFENSIVE_CENTRIST_DEMOCRACY
    assert nation.wa_status == WAStatus.DELEGATE
    assert nation.endorsements == ["nationalist_gold_union", "international_silver_combine"]
    assert nation.ga_vote == WAVote.UNDECIDED
    assert nation.sc_vote == WAVote.UNDECIDED
    assert nation.issues_answered == 146
    assert nation.region == "Testregionia"
    assert nation.population == 45032000000
    assert nation.tax == 87.7
    assert nation.animal == "★★★ nautilus ★★★"
    assert nation.animal_trait == "frolics freely in the nation's sparkling oceans"
    assert nation.currency == "Kro-bro-ünze"
    # assert nation.flag == "https://www.nationstates.net/images/flags/uploads/testlandia__656619.svg"
    assert nation.demonym_adjective == "Testlandian"
    assert nation.demonym == "Testlandian"
    assert nation.demonym_plural == "Testlandians"
    assert nation.gdp == 3028320312564630
    assert nation.income == 67248
    assert nation.richest == 81354
    assert nation.poorest == 54311
    assert nation.major_industry == MajorIndustry.INFORMATION_TECHNOLOGY
    assert nation.goverment_priority == GovernmentPriority.HEALTHCARE
    assert nation.budget.administration == 3.9
    assert nation.budget.defense == 11.9
    assert nation.budget.education == 20.6
    assert nation.budget.environment == 20.4
    assert nation.budget.healthcare == 24.4
    assert nation.budget.commerce == 4.8
    assert nation.budget.international_aid == 0.5
    assert nation.budget.law_and_order == 6.8
    assert nation.budget.public_transport == 3.2
    assert nation.budget.social_equality == 1.2
    assert nation.budget.spirituality == 0
    assert nation.budget.welfare == 2.2
