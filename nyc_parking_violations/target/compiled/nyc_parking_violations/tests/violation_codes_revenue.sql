

with __dbt__cte__silver_parking_violation_codes as (
WITH manhattan_violation_codes AS (
    SELECT
        violation_code,
        definition,
        TRUE AS is_manhattan_96th_st_below,
        manhattan_96th_st_below AS fee_usd,
    FROM
        "prod_nyc_parking_violations"."main"."bronze_parking_violation_codes"
),

all_other_violation_codes AS (
    SELECT
        violation_code,
        definition,
        FALSE AS is_manhattan_96th_st_below,
        all_other_areas AS fee_usd,
    FROM
        "prod_nyc_parking_violations"."main"."bronze_parking_violation_codes"
)

SELECT * FROM manhattan_violation_codes
UNION ALL
SELECT * FROM all_other_violation_codes
ORDER BY violation_code ASC
) select 
violation_code, 
sum(fee_usd) as total_revenue_usd
from 
__dbt__cte__silver_parking_violation_codes
group by violation_code
having 
not(total_revenue_usd >= 1)