class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = "".join(local.split("+")[0].split("."))
            unique.add((local, domain))
        return len(unique)
