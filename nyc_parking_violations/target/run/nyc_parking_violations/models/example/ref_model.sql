
  
  create view "nyc_parking_violations"."main"."ref_model__dbt_tmp" as (
    SELECT COUNT(*) from "nyc_parking_violations"."main"."first_model"
  );
