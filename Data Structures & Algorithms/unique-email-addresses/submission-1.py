class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer=set()

        for email in emails:

            local,domain=email.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")

            answer.add((local, domain))

        return len(answer)
