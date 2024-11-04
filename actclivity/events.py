class Activity:
    def __init__(self, events_data):
        self.events = []
        for event in events_data:
            self.events.append(Event(event))


class Repo:
    def __init__(self, repo):
        self.id = repo["id"]
        self.name = repo["name"]
        self.url = repo["url"]

    def __repr__(self):
        return f"{self.name}"


class Actor:
    def __init__(self, actor):
        self.id = actor["id"]
        self.login = actor["login"]
        self.display_login = actor["display_login"]
        self.gravatar_id = actor["gravatar_id"]
        self.url = actor["url"]
        self.avatar_url = actor["avatar_url"]

    def __repr__(self):
        return f"{self.display_login}"


class Event:
    def __init__(self, event):
        self.id = event["id"]
        self.type = event["type"]
        self.repo = Repo(event["repo"])
        self.payload = event["payload"]
        self.actor = Actor(event["actor"])
        self.time = event["created_at"]

    def __repr__(self):
        try:
            if self.type == "CommitCommentEvent":
                return f"Comment made on commit for {self.repo}"

            elif self.type == "CreateEvent":
                if self.payload["ref_type"] != "repository":
                    return f"Created {self.payload['ref_type']} '{self.payload['ref']}' '{self.repo}'"
                else:
                    return f"Created {self.payload['ref_type']} @{self.repo}"
            elif self.type == "DeleteEvent":
                return f"Deleted {self.payload['ref_type']} '{self.payload['ref']}' @{self.repo}"

            elif self.type == "ForkEvent":
                return f"Forked {self.repo}"
            elif self.type == "GollumEvent":
                result = ""
                for page in self.payload["pages"]:
                    result += f"{page['action']} wiki page '{page['title']}' "
                return f"{result.capitalize()} @{self.repo}"
            elif self.type == "IssueCommentEvent":
                if self.payload["action"] == "created":
                    return f"Made a comment ,{self.payload['comment']['html_url']}"
                elif self.payload["action"] == "edited":
                    return f"Edited comment ,{self.payload['comment']['html_url']}"
                elif self.payload["action"] == "deleted":
                    return f"Deleted comment saying '{self.payload['comment']['body']}'"
                else:
                    return f"{self.payload['action']} comment @{self.payload['comment']['html_url']}"
            elif self.type == "IssuesEvent":
                return f"{self.payload['action'].capitalize()} issue '{self.payload['issue']['title']}'"
            elif self.type == "MemberEvent":
                return f"{self.payload['action'].capitalize()} {self.payload['member']['login']}"
            elif self.type == "PublicEvent":
                return f"{self.repo} made public!"
            elif self.type == "PullRequestEvent":
                return f"{self.payload['action'].capitalize()} pull request #{self.payload['number']} @{self.repo}"
            elif self.type == "PullRequestReviewEvent":
                return f"{self.payload['action'].capitalize()} pull request review for #{self.payload['pull_request']['number']} @{self.repo}"
            elif self.type == "PullRequestReviewCommentEvent":
                return f"{self.payload['action'].capitalize()} comment on pull request #{self.payload['pull_request']['number']} @{self.repo}"
            # elif self.type == "PullRequestReviewThreadEvent":
            #     pass
            elif self.type == "PushEvent":
                return f"Pushed {self.payload['size']} commit(s) to '{self.payload['ref']}' {self.payload['push_id']} @{self.repo}"
            elif self.type == "ReleaseEvent":
                return f"{self.payload['action'].capitalize()} {self.payload['release']['body']} {self.payload['release']['name']} "
            elif self.type == "SponsorshipEvent":
                return f"{self.payload['action'.capitalize()]} Sponsership Event @{self.repo}"
            elif self.type == "WatchEvent":
                return f"Starred {self.repo}"
            else:
                return f"ERROR: output for '{self.type}' not defined"
        except:
            f"!ERROR:Event__repr__:{self.type}!"
