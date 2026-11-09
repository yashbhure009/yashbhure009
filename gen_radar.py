import math
# EDIT THESE (0-10) then run: python gen_radar.py
skills = [("Red Teaming",6),("VAPT",7),("Web AppSec",7),("SOC / Blue Team",6),("Cloud Security",6),("AI/ML Security",7)]
W,H,cx,cy,R = 560,420,280,215,130
n=len(skills)
def pt(i,r):
    a=-math.pi/2+2*math.pi*i/n
    return cx+r*math.cos(a), cy+r*math.sin(a)
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Consolas,Menlo,monospace">',
'<rect width="100%" height="100%" rx="12" fill="#0d1117"/>',
'<text x="280" y="34" text-anchor="middle" fill="#e6edf3" font-size="20" font-weight="bold">Security skill radar</text>',
'<text x="280" y="54" text-anchor="middle" fill="#8b949e" font-size="11">self-assessed, updated periodically</text>']
for lv in range(1,6):
    p=" ".join(f"{pt(i,R*lv/5)[0]:.1f},{pt(i,R*lv/5)[1]:.1f}" for i in range(n))
    o.append(f'<polygon points="{p}" fill="none" stroke="#30363d" stroke-width="1"/>')
for i in range(n):
    x,y=pt(i,R); o.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#30363d"/>')
p=" ".join(f"{pt(i,R*s/10)[0]:.1f},{pt(i,R*s/10)[1]:.1f}" for i,(_,s) in enumerate(skills))
o.append(f'<polygon points="{p}" fill="#00e5ff" fill-opacity="0.25" stroke="#00e5ff" stroke-width="2"><animate attributeName="fill-opacity" values="0.15;0.35;0.15" dur="4s" repeatCount="indefinite"/></polygon>')
for i,(name,s) in enumerate(skills):
    x,y=pt(i,R*s/10); o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#00e5ff"/>')
    lx,ly=pt(i,R+26)
    anc="middle" if abs(lx-cx)<5 else ("start" if lx>cx else "end")
    o.append(f'<text x="{lx:.1f}" y="{ly+4:.1f}" text-anchor="{anc}" fill="#e6edf3" font-size="12">{name}</text>')
o.append('</svg>')
open("assets/radar.svg","w").write("\n".join(o))
