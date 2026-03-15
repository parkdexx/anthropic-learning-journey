다음 Node.js 명령을 실행하고, 결과를 아래 형식으로 보여주세요.

```bash
node -e "
const cities = [
  ['🇰🇷 서울 (Seoul)',       'Asia/Seoul'],
  ['🇨🇳 남경 (Nanjing)',     'Asia/Shanghai'],
  ['🇹🇭 방콕 (Bangkok)',     'Asia/Bangkok'],
  ['🇪🇬 카이로 (Cairo)',     'Africa/Cairo'],
  ['🇨🇦 밴쿠버 (Vancouver)', 'America/Vancouver'],
];

const now = new Date();
for (const [city, tz] of cities) {
  const parts = new Intl.DateTimeFormat('en-CA', {
    timeZone: tz,
    year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', second: '2-digit',
    hour12: false,
    timeZoneName: 'short'
  }).formatToParts(now);
  const get = t => parts.find(p => p.type === t)?.value ?? '';
  const line = get('year')+'-'+get('month')+'-'+get('day')+' '+get('hour')+':'+get('minute')+':'+get('second')+' '+get('timeZoneName');
  console.log(city.padEnd(30) + line);
}
"
```

출력 형식:
```
🌏 세계 주요 도시 현재 시각
─────────────────────────────────────────────
🇰🇷 서울 (Seoul)          YYYY-MM-DD HH:MM:SS KST
🇨🇳 남경 (Nanjing)        YYYY-MM-DD HH:MM:SS CST
🇹🇭 방콕 (Bangkok)        YYYY-MM-DD HH:MM:SS +07
🇪🇬 카이로 (Cairo)        YYYY-MM-DD HH:MM:SS EET
🇨🇦 밴쿠버 (Vancouver)    YYYY-MM-DD HH:MM:SS PST
```
