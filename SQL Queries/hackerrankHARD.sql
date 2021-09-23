# Couldnt pass tests for some unapparent reason, fix it later

SELECT A.contest_id, A.hacker_id, A.name, SUM(total_submissions), SUM(total_accepted_submissions), SUM(total_views), SUM(total_unique_views)
FROM Contests as A
LEFT JOIN Colleges as B
LEFT JOIN Challenges as C
LEFT JOIN (SELECT challenge_id, 
      SUM(total_views) AS total_views, 
      SUM(total_unique_views) as total_unique_views
      FROM View_Stats
      GROUP BY challenge_id
      ORDER BY challenge_id
     )as D
LEFT JOIN (SELECT challenge_id, 
      SUM(total_submissions) AS total_submissions, 
      SUM(total_accepted_submissions) as total_accepted_submissions
      FROM Submission_Stats
      GROUP BY challenge_id
      ORDER BY challenge_id
     )as E
ON (A.contest_id = B.contest_id)
AND (B.college_id = C.college_id) 
AND (C.challenge_id = D.challenge_id)
AND (D.challenge_id = E.challenge_id)
GROUP BY 
        A.contest_id, 
        A.hacker_id, 
        A.name
HAVING 
    (total_submissions + total_accepted_submissions + total_views + total_unique_views) > 0 
ORDER BY 
        A.contest_id;

