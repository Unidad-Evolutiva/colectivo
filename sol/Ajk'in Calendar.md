# Proposal for a New Calendar: "Ajk’in Calendar"
## Version May 18, 2025, 15:15:00 UTC-03

## 1. Introduction

The **Ajk’in Calendar** is a proposed linear cumulative solar timekeeping system that, like the Mayan Haab' calendar, is based on an annual cycle of **365 days**. This calendar divides the year into **13 months**, each named after the **13 zodiacal constellations**, including Ophiuchus. The starting date is set as **December 22, 2012**, symbolizing a cosmic renewal in the Mayan tradition.

## 2. Origin and Justification

As an extension of the Gregorian calendar, its use aligns with astronomical cycles and the cultural symbolism of various traditions. The Ajk’in Calendar proposes an alternative that, while maintaining the **365-day** annual duration of the Haab', offers a different structure and a direct astronomical connection:

* Starting date: December 22, 2012 (Ajk’in Day 1)
* 13 months (derived from the zodiacal constellations) per year with a leap adjustment in one month
* Annual duration of 365 days (366 in leap years), like the Mayan Haab' calendar

## 3. Calendar Structure

**Main features:**

* **Starting date:** December 22, 2012 (Ajk’in Day 1)
* **Base unit:** 1 day
* **Year duration:** **365 days** (366 in leap years)
* **Months per year:** 13
* **Normal month duration:** 12 months × 28 days + **Virgo × 29 days**
* **Leap year month duration:** 11 months × 28 days + **Virgo × 29 days** + **Leo × 29 days**
* **Month names:** Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Ophiuchus, Sagittarius, Capricorn, Aquarius

### 3.1 Note on Counting and Year Duration

The Ajk’in Calendar adopts a **linear and cumulative counting** of days. The base year has a duration of 365 days but is periodically adjusted through the **Ajk’in Leap Day** incorporated into the month of Leo to maintain synchronization with the solar year. To achieve long-term astronomical precision, it also incorporates a nested cyclic correction system designed to reach exactly **1,872,000,000,000 days** over a period of **5,128,767,123 years**. This system operates under the following inverted and renamed hierarchy of cycles:

* **Solar Cycle (Level 0):** **+97 days are added every 400 years through leap days**. Over the span of 146,097 days, this would add approximately 97 days.

    $$\frac{5,\!128,\!767,\!123}{400} \approx 12,\!821,\!918$$

* **Stellar Cycle (Level 1):** **+1 day is added every 5,128 years**. Over the span of 5,128,767,123 years, this would add approximately 1,000,195 days. These days are added to those already included by the previous cycle.

    $$\frac{5,\!128,\!767,\!123}{5,\!128} \approx 1,\!000,\!195$$

* **Galactic Cycle (Level 2):** **+1 day is added every 194,978 years**. This cycle adds approximately 26,307 days over the total period. These days are added to those already included by the previous cycles.

    $$\frac{5,\!128,\!767,\!123}{194,\!978} \approx 26,\!307$$

* **Cosmic Cycle (Level 3):** **+1 day is added every 48,845,401 years**. Over the span of 5,128,767,123 years, this results in exactly 105 days added. These days are added to those already included by the previous cycles.

    $$\frac{5,\!128,\!767,\!123}{48,\!845,\!401} = 105$$

### 3.2 Ajk’in Leap Day: Adjustment for the Solar Year

To achieve greater precision with respect to the actual solar year (~365.2422 days) on human time scales, the Ajk’in Calendar incorporates an **Ajk’in Leap Day** system. This additional day is added to the month of Leo, extending its duration to 29 days in certain years. The rule for determining when the month of Leo has 29 days (leap year) is as follows:

* The month of Leo has 29 days if the Ajk’in year number is divisible by 4.
* However, the month of Leo has 28 days if the Ajk’in year is divisible by 100, unless it is also divisible by 400.

## 4. Conversion Between Gregorian and Ajk’in Calendars

* Days are counted consecutively, advancing through the months and years according to the fixed calendar structure, with the occasional addition of a day to the month of Leo in leap years.
* **Ajk’in Day 0:** December 21, 2012 (for reference only; not officially counted)
* **Ajk’in Day 1:** December 22, 2012 (official calendar start)

## 5. Precision in Calculations

The Ajk’in Day is determined by counting consecutive days from December 22, 2012 (Day 1).  
Leap years: Align with Gregorian leap years (years divisible by 4, except those divisible by 100 but not by 400).  
Extra day in Leo: The 29th day in leap years is already included when counting the days of February 29 in the Gregorian calendar in the total calculation.

**Basic formula:**

Ajk’in Day = (Gregorian Date - December 21, 2012) in total days

## 6. Conversion Example

| Gregorian Date | Ajk’in Day | Year | Month No. | Month Name | Day of Month | Notes        |
|----------------|------------|------|-----------|------------|--------------|--------------|
| Dec 21, 2012   | 0          | -    | -         | -          | -            | Node         |
| Dec 22, 2012   | 1          | 1    | 1         | Pisces     | 1            | Start        |
| Feb 29, 2024   | 4087       | 12   | 6         | Leo        | 29           | Leap year    |
| Jun 28, 2025   | 4572       | 13   | 6         | Leo        | 28           | Normal       |

## 7. Advantages

* Alignment with astronomical reality through the use of zodiacal constellations.
* Nearly uniform annual structure that simplifies time tracking.
* Significant starting date with symbolic and cultural value.
* Shares some cycles with the Mayan Haab' calendar and the fundamental duration of the solar year.
* Excellent precision with the solar year due to the addition of a leap day in the month of Leo.
* **Incorporates a long-term correction system with an inverted and renamed hierarchy of cycles (Stellar -> Galactic -> Cosmic) that ensures the accuracy of 1,872,000,000,000 days over a period of 5,128,767,123 years, offering remarkable synchrony with the Mayan Long Count in this vast cycle.**
* Symbolic integration of the leap day in the month of Leo.

## 8. Implementation and Dissemination

The development of the following is recommended:

* Educational resources explaining the annual structure, the leap day rules for Leo, long-term cycles, and date conversion.
* Calendar converters and visual tools that account for leap years and the variable duration of Leo.
* Pilot implementations in cultural, academic, or scientific institutions.

## 9. Contact

**Proposal submitted by:**

Scolari, Mauricio H. J.  
Email: [mauricio@scolari.org](mailto:mauricio@scolari.org)  
Phone: +54 9 341 3080606
