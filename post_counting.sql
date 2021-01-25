SELECT 
Year(DATE) as YEAR, 
Month(DATE) as MONTH, 
sum(IIF(Trump_mention = 'Y', 1, 0)) as YES_TRUMP, 
sum(IIF(Trump_mention = 'N', 1, 0)) as NO_TRUMP,
sum(IIF(Trump_mention = 'Y' AND Curse_used = 'Y', 1, 0)) as TRUMP_CURSE,
sum(IIF(Trump_mention = 'N' AND Curse_used = 'Y', 1, 0)) as NO_TRUMP_CURSE
INTO post_counts
FROM post_2016_2021
GROUP BY Year(DATE), Month(DATE)
ORDER BY YEAR, MONTH;