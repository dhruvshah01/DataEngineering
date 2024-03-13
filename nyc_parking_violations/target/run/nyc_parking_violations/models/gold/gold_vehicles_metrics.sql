
  
  create view "prod_nyc_parking_violations"."main"."gold_vehicles_metrics__dbt_tmp" as (
    SELECT
registration_state,
count(summons_number) as ticket_count
FROM
"prod_nyc_parking_violations"."main"."silver_violation_vehicles"
WHERE
registration_state != 'NY'
GROUP BY
registration_state
ORDER BY
ticket_count DESC
  );
