from ai_commerce_os.agents.ceo.prompts import SYSTEM_PROMPT, USER_PROMPT


def test_prompt_placeholders_are_empty() -> None:
    assert SYSTEM_PROMPT == ""
    assert USER_PROMPT == ""
