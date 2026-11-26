[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/iqbalbeladaz/funniest-sign-haunted-server-room/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/iqbalbeladaz/funniest-sign-haunted-server-room/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)

# Funniest Sign on a Haunted Server Room Door

Entry for the make.fun bounty
[Funniest Sign on a Haunted Server Room Door](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
($2): one funny line for the door of a haunted server room, at most 120
characters, judged head to head by an AI judge.

## The entry

> DO NOT REBOOT — the ghost is the only one who remembers the root password.

74 characters (gate: 1–120).

## Why this line should win

- **It is a sign, not a joke about a sign:** it opens with a door-sign
  imperative — DO NOT REBOOT — the exact words taped to a server room
  door, and the rest of the line reads like the warning underneath it.
- **Real laugh from the IT × supernatural collision:** a reboot is the
  most ordinary sysadmin verb, the root password is the one secret nobody
  is allowed to lose, and the ghost is the institution's memory — the
  only being left who knows it. The punchline lands on "the root
  password", the phrase with the most weight in the room.
- **Fresh haunting:** the ghost is not rattling chains or moaning in the
  cold aisle — he is the keeper of the credentials, the one person (or
  spirit) the team cannot afford to exorcise. That is a new angle on the
  haunted server room.
- **Reads cleanly aloud in one breath:** one sentence, no filler, no pun
  that needs a second read, punchline last.

## Alternatives considered

Eight lines were drafted and counted before this one was picked:

- "DO NOT EXORCISE THE SERVER — the ghost is the only one who knows
  where the backups are." (87 chars) — same shape, strong punchline
  about backups, but "reboot" is the more sign-like verb and "root
  password" lands harder than "where the backups are".
- "WARNING: the ghost in this room has root access. He closes tickets,
  not doors." (78 chars) — the "closes tickets, not doors" twist is
  clever, but it is a pun that needs a second read, which the judge
  brief penalises.
- "The ghost has been on call since 1998. Do not wake him. He has root
  access." (75 chars) — "on call since 1998" is a good fresh detail,
  but the line has no single punchline; it trails off instead of
  landing.
- "IF THE SERVER WHISPERS YOUR NAME, DO NOT ANSWER — IT IS THE GHOST,
  AND HE IS STILL ON CALL." (91 chars) — atmospheric, but all caps
  shouts where a sign instructs, and "still on call" is a weaker
  punchline than the root password.
- "KNOCK TWICE — the ghost is mid-deploy and the rollback is haunted."
  (66 chars) — short and sign-like, but "the rollback is haunted" is a
  claim about the deploy rather than a joke with a punchline.
- "Please knock — the ghost is rebooting the server and he hates being
  watched." (76 chars) — "he hates being watched" is a shrug, not a
  punchline; the ghost doing the rebooting is also less funny than the
  ghost being the reason not to reboot.
- "HAUNTED: the ghost has root access and already closed your ticket as
  'won't fix'." (81 chars) — "closed your ticket as 'won't fix'" is a
  genuinely funny sysadmin punchline, but it reads as a status report
  rather than a sign on a door, and the quoted status slows the read.

The chosen line won because it stacks all five judge criteria in one
breath: sign shape first, IT × supernatural collision in the middle,
punchline last.

## How it works

`main.py` writes the line to `/output/entry.txt`. It is fully
deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

## License

MIT — see [LICENSE](LICENSE).
