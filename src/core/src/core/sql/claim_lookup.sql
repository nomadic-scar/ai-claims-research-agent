SELECT
    claim_id,
    status,
    denial_reason,
    benefit_rule
FROM claims
WHERE claim_id = :claim_id;
