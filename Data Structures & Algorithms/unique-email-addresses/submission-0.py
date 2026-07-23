class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@", 1)
            local = local.split("+", 1)[0].replace(".", "")
            unique.add(local + "@" + domain)
        
        return len(unique)
        