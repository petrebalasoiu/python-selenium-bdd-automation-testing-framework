Feature: Top HUD
  Background:
    Given the user is anywhere on the website

  @T1
  Scenario: Verify the behaviour of the first top HUD button from left to right
    # "Telefon pentru comenzi: 0764.378.979"
    When the user clicks the first top HUD button from left to right
    Then a new tab opens with the Whatsapp connection link

  @T2
  Scenario: Verify the behaviour of the second top HUD button from left to right
    # "Livrare gratuita pentru comenzile de 200+ lei"
    When the user clicks the second top HUD button from left to right
    Then a new tab opens with a copy of the original page

  @T3
  Scenario: Verify the behaviour of the third top HUD button from left to right
    # "Urmareste-ne pe Facebook"
    When the user clicks the third top HUD button from left to right
    Then a new tab opens with the company's Facebook page

  @T4
  Scenario: Verify the behaviour of the fourth top HUD button from left to right
    # "Urmareste-ne pe Instagram"
    When the user clicks the fourth top HUD button from left to right
    Then a new tab opens with the company's Instagram page