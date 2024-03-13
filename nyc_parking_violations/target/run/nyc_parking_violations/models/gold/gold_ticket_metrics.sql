
  
  create view "prod_nyc_parking_violations"."main"."gold_ticket_metrics__dbt_tmp" as (
    SELECT
violation_code,
count(summons_number) as ticket_count,
sum(fee_usd) as total_revenue
FROM 
"prod_nyc_parking_violations"."main"."silver_violation_tickets"
GROUP BY
violation_code
ORDER BY
total_revenue DESC
  );
