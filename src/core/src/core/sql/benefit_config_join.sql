SELECT
    c.claim_id,
    c.status,
    c.denial_reason,
    b.rule_id,
    b.rule_description,
    b.requirements,
    b.step_therapy_group
FROM claims c
LEFT JOIN benefit_rules b
    ON c.benefit_rule = b.rule_id
WHERE c.claim_id = :claim_id;
