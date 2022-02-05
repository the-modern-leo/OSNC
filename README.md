# OSNC
Open Source Network Controller

Step 1: 
docker build '/Users/nickbradberry/PycharmProjects/OSNC/' -t onsc:latest

Step2:
docker run -v '/Users/nickbradberry/PycharmProjects/OSNC/':/opt/project -p 443:8443 onsc:latest 



Project is being built with the following features: 
A containerized web server. The webserver python Tornado 

Full Device Support:
<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">
<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 15">
<link rel=File-List href="Full_device_support.fld/filelist.xml">
<style id="Full_device_support_21875_Styles">
<!--table
	{mso-displayed-decimal-separator:"\.";
	mso-displayed-thousand-separator:"\,";}
@page
	{margin:.75in .7in .75in .7in;
	mso-header-margin:.3in;
	mso-footer-margin:.3in;}
tr
	{mso-height-source:auto;}
col
	{mso-width-source:auto;}
br
	{mso-data-placement:same-cell;}
.style0
	{mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	white-space:nowrap;
	mso-rotate:0;
	mso-background-source:auto;
	mso-pattern:auto;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;
	border:none;
	mso-protection:locked visible;
	mso-style-name:Normal;
	mso-style-id:0;}
td
	{mso-style-parent:style0;
	padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;
	mso-protection:locked visible;
	white-space:nowrap;
	mso-rotate:0;}
.xl65
	{mso-style-parent:style0;
	font-weight:700;}
-->
</style>
</head>
<body link=blue vlink=purple>
<div id="Full_device_support_21875" align=center x:publishsource="Excel">
<table border=0 cellpadding=0 cellspacing=0 width=1601 style='border-collapse:
 collapse;table-layout:fixed;width:1201pt'>
 <col width=372 style='mso-width-source:userset;mso-width-alt:11904;width:279pt'>
 <col width=117 style='mso-width-source:userset;mso-width-alt:3754;width:88pt'>
 <col width=249 style='mso-width-source:userset;mso-width-alt:7978;width:187pt'>
 <col width=148 style='mso-width-source:userset;mso-width-alt:4736;width:111pt'>
 <col width=243 style='mso-width-source:userset;mso-width-alt:7765;width:182pt'>
 <col width=472 style='mso-width-source:userset;mso-width-alt:15104;width:354pt'>
 <tr height=20 style='height:15.0pt'>
  <td height=20 class=xl65 width=372 style='height:15.0pt;width:279pt'>DNS</td>
  <td class=xl65 width=117 style='width:88pt'>IP Address</td>
  <td class=xl65 width=249 style='width:187pt'>Vendor</td>
  <td class=xl65 width=148 style='width:111pt'>Model</td>
  <td class=xl65 width=243 style='width:182pt'>IOS Image</td>
  <td class=xl65 width=472 style='width:354pt'>IOS Version</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-ddc-i11.net.utah.edu</td>
  <td>172.28.65.82</td>
  <td>Cisco</td>
  <td>N5K-C5020P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx2-ddc-j11.net.utah.edu</td>
  <td>172.28.65.83</td>
  <td>Cisco</td>
  <td>N5K-C5020P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>ddr1-ddc-i13-mgmt.net.utah.edu</td>
  <td>172.29.1.22</td>
  <td>Cisco</td>
  <td>N7K-C7010</td>
  <td>n7000-s1-dk9</td>
  <td>6.2(16)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-ddc-m4.net.utah.edu</td>
  <td>172.28.65.86</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx2-ddc-m4.net.utah.edu</td>
  <td>172.28.65.87</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3574ddc-114-1a-ebc.net.utah.edu</td>
  <td>172.31.9.13</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3574ddc-j11.net.utah.edu</td>
  <td>172.31.9.10</td>
  <td>Cisco</td>
  <td>WS-C3750G-24TS-E</td>
  <td>C3750-IPBASEK9-M</td>
  <td>12.2(58)SE2</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3574ddc-pumphouse-ebc.net.utah.edu</td>
  <td>172.31.9.11</td>
  <td>Cisco</td>
  <td>WS-C3650-24PD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx4-ddc-j11.net.utah.edu</td>
  <td>172.28.65.93</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.1(3)N2(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>scx1-ddc-m5.net.utah.edu</td>
  <td>172.31.224.12</td>
  <td>Cisco</td>
  <td>WS-C2960-24TT-L</td>
  <td>C2960-LANBASEK9-M</td>
  <td>12.2(52)SE</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-ddc-m12.net.utah.edu</td>
  <td>172.28.65.94</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(8a)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx2-ddc-m12.net.utah.edu</td>
  <td>172.28.65.95</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(8a)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3574ddc-hirc-ebc.net.utah.edu</td>
  <td>172.31.9.4</td>
  <td>Cisco</td>
  <td>WS-C3650-48FQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-529eccp-pa080-clinical.net.utah.edu</td>
  <td>172.20.62.4</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-851uuoc-a0318-clinical.net.utah.edu</td>
  <td>172.20.28.10</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.08.05.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3587obgynlds-1-remote.net.utah.edu</td>
  <td>172.29.0.10</td>
  <td>Cisco</td>
  <td>WS-C3650-48PD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx2-529eccp-p5009-clinical.net.utah.edu</td>
  <td>172.20.62.5</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.07.01.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3113midvalley-2151a-remote.net.utah.edu</td>
  <td>172.20.91.4</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500e-UNIVERSALK9-M</td>
  <td>03.11.03a.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-525hosp-b244-clinical.net.utah.edu</td>
  <td>172.20.64.69</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-561hnpth-1300-clinical.net.utah.edu</td>
  <td>172.20.60.23</td>
  <td>Cisco</td>
  <td>WS-C3650-24PD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.06.06E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-904.net.utah.edu</td>
  <td>172.20.241.72</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500e-UNIVERSALK9-M</td>
  <td>03.04.03.SG<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-523moran-s1615.med.utah.edu</td>
  <td>172.20.245.12</td>
  <td>Cisco</td>
  <td>WS-C3650-48FQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-523moran-a0275.med.utah.edu</td>
  <td>172.20.245.11</td>
  <td>Cisco</td>
  <td>WS-C3650-48PQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.07.02E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-550cnc-1285.med.utah.edu</td>
  <td>172.20.60.11</td>
  <td>Cisco</td>
  <td>WS-C3650-48PQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.06.06E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-550cnc-3280.med.utah.edu</td>
  <td>172.20.60.12</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.07.00.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>scx1-865williams-dc-peds.net.utah.edu</td>
  <td>172.20.254.19</td>
  <td>Cisco</td>
  <td>C9300-48UXM</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-521som-ab193.net.utah.edu</td>
  <td>172.20.66.11</td>
  <td>Brocade Communications Systems, Inc.</td>
  <td></td>
  <td></td>
  <td>04.0.00aTc1 Compiled on Mar 13 2008 at 00:47:41 labeled as FES04000a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-521som-4b319d-clinical.net.utah.edu</td>
  <td>172.20.66.70</td>
  <td>Brocade Communications Systems, Inc.</td>
  <td></td>
  <td></td>
  <td>04.1.01eTc1 Compiled on Mar 06 2011 at 17:05:36 labeled as FES04101e</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3701sjhc-128-sjhc.net.utah.edu</td>
  <td>172.20.72.199</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.9.2,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3701sjhc-308-sjhc.net.utah.edu</td>
  <td>172.20.72.201</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-521som-1b449-som.net.utah.edu</td>
  <td>172.20.66.29</td>
  <td>Cisco</td>
  <td>C9300-48P</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-521som-3c340a-w-som.net.utah.edu</td>
  <td>172.20.66.9</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>17.3.3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sw-521-gcrc.med.utah.edu</td>
  <td>172.20.66.74</td>
  <td>Cisco</td>
  <td>WS-C3650-48FWQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-521som-3r210d.net.utah.edu</td>
  <td>172.20.66.54</td>
  <td>Brocade Communications Systems, Inc.</td>
  <td></td>
  <td></td>
  <td>04.1.01hTc1 Compiled on Feb 11 2014 at 10:08:11 labeled as FES04101h</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-865williams-2n920-clinical.net.utah.edu</td>
  <td>172.20.254.37</td>
  <td>Cisco</td>
  <td>WS-C2960S-48FPD-L</td>
  <td>C2960S-UNIVERSALK9-M</td>
  <td>12.2(55)SE7</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-525hosp-2741-clinical.net.utah.edu</td>
  <td>172.20.64.16</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-525hosp-4270-clinical.net.utah.edu</td>
  <td>172.20.64.58</td>
  <td>Cisco</td>
  <td>WS-C3650-48PQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.07.03E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-888inc-1251-a1-clinical.net.utah.edu</td>
  <td>172.20.125.26</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.5b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-904redwood-2-breakroom-redwood.net.utah.edu</td>
  <td>172.20.241.71</td>
  <td>Cisco</td>
  <td>WS-C3650-48FS-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.3.6</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-904redwood-main.med.utah.edu</td>
  <td>172.20.241.69</td>
  <td>Cisco</td>
  <td>WS-C3650-48FS-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.06.06E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-521som-ac142d.net.utah.edu</td>
  <td>172.20.66.64</td>
  <td>Brocade Communications Systems, Inc.</td>
  <td></td>
  <td></td>
  <td>04.3.02bT7e1 Compiled on Sep 21 2009 at 15:52:58 labeled as FGS04302b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-521som-1r35-clinical.net.utah.edu</td>
  <td>172.20.66.114</td>
  <td>Brocade Communications Systems, Inc.</td>
  <td></td>
  <td></td>
  <td>04.1.01dTc1 Compiled on Nov 11 2010 at 15:45:59 labeled as FES04101d</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-857-421wakara-103.net.utah.edu</td>
  <td>172.31.4.103</td>
  <td>Cisco</td>
  <td>WS-C2960XR-48FPD-I</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.2(2)E7</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-525hosp-services-clinical.net.utah.edu</td>
  <td>172.20.176.4</td>
  <td>Cisco</td>
  <td>C9300-48P</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3031unigtc-a2-remote.net.utah.edu</td>
  <td>172.20.71.197</td>
  <td>Cisco</td>
  <td>WS-C2960XR-48FPS-I</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.2(4)E6,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3522ars-3comm-remote.net.utah.edu</td>
  <td>172.20.12.4</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-918centerville.net.utah.edu</td>
  <td>172.20.241.4</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500e-UNIVERSALK9-M</td>
  <td>03.06.06.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-521som-bc01-som.net.utah.edu</td>
  <td>172.20.66.4</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>17.3.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-0085heb-b0172-park.net.utah.edu</td>
  <td>172.30.131.197</td>
  <td>Cisco</td>
  <td>WS-C3650-12X48UQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-040ssb-2south.net.utah.edu</td>
  <td>155.101.126.208</td>
  <td>Cisco</td>
  <td>WS-C3650-48FD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-044bldg44-200m-park.net.utah.edu</td>
  <td>172.30.128.68</td>
  <td>Cisco</td>
  <td>C9300-48UXM</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.3a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>scx2-0001park-150-a07-ebc.net.utah.edu</td>
  <td>155.101.202.43</td>
  <td>Cisco</td>
  <td>WS-C3650-24PD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.3.5b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-001park-ebc.net.utah.edu</td>
  <td>155.101.202.41</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(9)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-001park-ebc.net.utah.edu</td>
  <td>155.101.202.42</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(9)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-2460va-2eac-1a-ebc.net.utah.edu</td>
  <td>172.31.12.9</td>
  <td>Cisco</td>
  <td>C9300-24U</td>
  <td>CAT9K_IOSXE</td>
  <td>17.3.3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3464va2-1b07-ebc.net.utah.edu</td>
  <td>172.31.12.37</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(4)E4,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-2460va-1b29-w-ebc.net.utah.edu</td>
  <td>172.31.12.8</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(7)E3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-036umfa-001-lib-poe.net.utah.edu</td>
  <td>155.97.24.42</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(4)E5,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-822bnch-usa-towers.net.utah.edu</td>
  <td>155.97.252.132</td>
  <td>Cisco</td>
  <td>C9300-24U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-775usa-east.net.utah.edu</td>
  <td>155.97.252.212</td>
  <td>Adtran</td>
  <td></td>
  <td></td>
  <td></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-605ehs.net.utah.edu</td>
  <td>155.97.255.165</td>
  <td>Cisco</td>
  <td>WS-C3650-48PQ-L</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-327greenhouse.net.utah.edu</td>
  <td>155.97.255.92</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(7)E2</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-064eng.net.utah.edu</td>
  <td>155.98.126.70</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(4)E2,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r1-voice.net.utah.edu</td>
  <td>155.99.131.16</td>
  <td>Cisco</td>
  <td>C6880-X</td>
  <td>c6880x-ADVENTERPRISEK9-M</td>
  <td>15.5(1)SY7,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>rr-179ebc-070.net.utah.edu</td>
  <td>155.99.132.160</td>
  <td>Cisco</td>
  <td>ASR1001-X</td>
  <td>X86_64_LINUX_IOSD-UNIVERSALK9-M</td>
  <td>15.6(1)S2</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-489bsb-2-remote.net.utah.edu</td>
  <td>172.20.58.100</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500e-UNIVERSALK9-M</td>
  <td>03.04.01.SG<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx2-179ebc-wan.net.utah.edu</td>
  <td>172.29.0.40</td>
  <td>Cisco</td>
  <td>N5K-C5010P-BF</td>
  <td>n5000-uk9</td>
  <td>5.1(3)N1(1a)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r1-park-179ebc-070.net.utah.edu</td>
  <td>172.29.1.12</td>
  <td>Cisco</td>
  <td>C9606R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.5b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r2-park-001park-150.net.utah.edu</td>
  <td>172.29.1.13</td>
  <td>Cisco</td>
  <td>C9606R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.5b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>cr-179ebc-070-mgmt.net.utah.edu</td>
  <td>172.29.1.30</td>
  <td>Cisco</td>
  <td></td>
  <td>n7000-s2-dk9</td>
  <td>7.3(2)D1(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>cr-001park-150-mgmt.net.utah.edu</td>
  <td>172.29.1.31</td>
  <td>Cisco</td>
  <td></td>
  <td>n7000-s2-dk9</td>
  <td>7.3(2)D1(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-071saec-0200-lib.net.utah.edu</td>
  <td>172.30.5.4</td>
  <td>Cisco</td>
  <td>C9500-16X</td>
  <td>CAT9K_IOSXE</td>
  <td>17.3.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-585radlab-55a.net.utah.edu</td>
  <td>172.31.0.69</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(4)E3,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-112mrsc-5-fort.net.utah.edu</td>
  <td>172.31.128.134</td>
  <td>Cisco</td>
  <td>WS-C4506-E</td>
  <td>cat4500e-UNIVERSALK9-M</td>
  <td>03.11.03a.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-151ustar-2233.net.utah.edu</td>
  <td>172.31.2.143</td>
  <td>Cisco</td>
  <td>WS-C2960S-24PS-L</td>
  <td>C2960S-UNIVERSALK9-M</td>
  <td>12.2(55)SE3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-151ustar.net.utah.edu</td>
  <td>172.31.2.132</td>
  <td>Cisco</td>
  <td>WS-C4507R+E</td>
  <td>cat4500e-UNIVERSALK9-M</td>
  <td>03.11.03a.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-302hightemp.net.utah.edu</td>
  <td>172.31.5.228</td>
  <td>Cisco</td>
  <td>C9300-24P</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-582pharm-b0421-a1-ebc.net.utah.edu</td>
  <td>172.31.7.132</td>
  <td>Cisco</td>
  <td>C9500-48Y4C</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-582pharm-itoffice-ebc.net.utah.edu</td>
  <td>172.31.7.157</td>
  <td>Cisco</td>
  <td>WS-C2960XR-48FPD-I</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.2(2)E7</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-369ambulparking-p3.net.utah.edu</td>
  <td>172.31.8.180</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.8.1a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-369ambulparking-p3.net.utah.edu</td>
  <td>172.31.8.181</td>
  <td>Cisco</td>
  <td>IE-3000-8TC</td>
  <td>IES-LANBASEK9-M</td>
  <td>15.0(2)EY1</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>new-vpnaccess-mgmt.net.utah.edu</td>
  <td>172.29.1.69</td>
  <td>Cisco</td>
  <td></td>
  <td></td>
  <td>9.8(4)15</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-0489bsb-101p-bsb.net.utah.edu</td>
  <td>172.20.58.102</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500e-UNIVERSALK9-M</td>
  <td>03.04.04.SG<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>vpn-hsc-active-inside.med.utah.edu</td>
  <td>10.104.65.22</td>
  <td>Cisco</td>
  <td>ASA5555</td>
  <td></td>
  <td>9.8(4)15</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-va-45-ga04.net.utah.edu</td>
  <td>172.31.12.25</td>
  <td>Cisco</td>
  <td>WS-C2960X-24PS-L</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.0(2)EX5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-va-2-gc13.net.utah.edu</td>
  <td>172.31.12.26</td>
  <td>Cisco</td>
  <td>WS-C2960X-48LPS-L</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.2(2)E6</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-va-2-1c29.net.utah.edu</td>
  <td>172.31.12.27</td>
  <td>Cisco</td>
  <td>WS-C2960X-48LPS-L</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.0(2)EX5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-001park-150-parkservices-park.net.utah.edu</td>
  <td>155.101.126.151</td>
  <td>Cisco</td>
  <td>WS-C3650-48PQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>vpn-p2p-hsc-inside.med.utah.edu</td>
  <td>10.104.65.20</td>
  <td>Cisco</td>
  <td>ASA5555</td>
  <td></td>
  <td>9.8(4)10</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-090jhc-cloud-ebc.net.utah.edu</td>
  <td>172.31.5.200</td>
  <td>Cisco</td>
  <td>C9300-24U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-908stansbury-sb.net.utah.edu</td>
  <td>172.20.241.34</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.08.07.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-179ebc-services-ebc.net.utah.edu</td>
  <td>172.31.10.100</td>
  <td>Cisco</td>
  <td>WS-C3650-48PQ</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.07.00E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3647sweetwater-1d22-vpn.net.utah.edu</td>
  <td>172.24.8.82</td>
  <td>Cisco</td>
  <td>WS-C3560CG-8PC-S</td>
  <td>C3560c405ex-UNIVERSALK9-M</td>
  <td>12.2(55)EX2</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r1-remote-ddc.net.utah.edu</td>
  <td>172.29.4.1</td>
  <td>Cisco</td>
  <td>C6880-X</td>
  <td>c6880x-ADVENTERPRISEK9-M</td>
  <td>15.5(1)SY1</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-512rab-011-ebc.net.utah.edu</td>
  <td>172.20.247.14</td>
  <td>Cisco</td>
  <td>WS-C3850-12X48U-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>tr-179ebc-mgmt.net.utah.edu</td>
  <td>172.29.1.120</td>
  <td>Cisco</td>
  <td>ASR1001-X</td>
  <td>X86_64_LINUX_IOSD-UNIVERSALK9-M</td>
  <td>15.4(3)S3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-483-525plaza-4-5080-remote.net.utah.edu</td>
  <td>172.23.1.74</td>
  <td>Cisco</td>
  <td>WS-C3650-48FQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.06.08E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx2-ddc-m3.net.utah.edu</td>
  <td>172.28.65.102</td>
  <td>Cisco</td>
  <td>N9K-C9332PQ</td>
  <td>n9000-dk9</td>
  <td>7.0(3)I1(2)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-ddc-m3.net.utah.edu</td>
  <td>172.28.65.101</td>
  <td>Cisco</td>
  <td>N9K-C9332PQ</td>
  <td>n9000-dk9</td>
  <td>7.0(3)I1(2)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx2-001park-parkservices-park.net.utah.edu</td>
  <td>155.101.126.152</td>
  <td>Cisco</td>
  <td>WS-C3650-48FQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.06.05E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-032stad-155police-lib.net.utah.edu</td>
  <td>172.30.9.14</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(3)E3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw1-3647sweetwater-1d22.net.utah.edu</td>
  <td>172.24.8.81</td>
  <td>Cisco</td>
  <td>ASA5506</td>
  <td></td>
  <td>9.5(1)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>vpn-athletics-mgmt.net.utah.edu</td>
  <td>172.29.2.104</td>
  <td>Cisco</td>
  <td></td>
  <td></td>
  <td>9.8(4)15</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3716farmington-111.net.utah.edu</td>
  <td>172.20.13.149</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.06.05.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-va-1-1eac-ebc.net.utah.edu</td>
  <td>172.31.12.33</td>
  <td>Cisco</td>
  <td>WS-C3650-24TD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-522wpav-wm320-clinical.net.utah.edu</td>
  <td>172.20.84.18</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.09.00.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-0484danjones-593-remote.net.utah.edu</td>
  <td>172.31.3.4</td>
  <td>Cisco</td>
  <td>WS-C3850-12XS-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx3-ddc-m4.net.utah.edu</td>
  <td>172.28.65.89</td>
  <td>Cisco</td>
  <td>N5K-C5020P-BF</td>
  <td>n5000-uk9</td>
  <td>5.2(1)N1(8a)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-064meb-4550-park.net.utah.edu</td>
  <td>172.30.131.101</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(4)E1,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw-440icse-1.net.utah.edu</td>
  <td>172.30.128.97</td>
  <td>Cisco</td>
  <td></td>
  <td></td>
  <td>9.8(2)38</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-522wpav-wm320-clinical.net.utah.edu</td>
  <td>172.20.84.5</td>
  <td>Cisco</td>
  <td>WS-C3850-24XS-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.07.04E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-522wpav-w1665-clinical.net.utah.edu</td>
  <td>172.20.84.26</td>
  <td>Cisco</td>
  <td>WS-C3850-48F-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.06.06E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3516slchangar-airmed.net.utah.edu</td>
  <td>172.29.2.196</td>
  <td>Cisco</td>
  <td>WS-C3650-24PD</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.07.00E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-0489bsb-200y-bsb.net.utah.edu</td>
  <td>172.20.58.107</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(7)E4,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r2-wifi-001park-150.net.utah.edu</td>
  <td>172.29.1.21</td>
  <td>Cisco</td>
  <td></td>
  <td>n7700-s2-dk9</td>
  <td>8.2(2)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-032stad-w-parkinglot-lib.net.utah.edu</td>
  <td>172.30.9.13</td>
  <td>Cisco</td>
  <td></td>
  <td>C3560c405ex-UNIVERSALK9-M</td>
  <td>15.0(2)SE5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3031unigtc-a2-remote.net.utah.edu</td>
  <td>172.20.71.199</td>
  <td>Cisco</td>
  <td>WS-C2960X-48LPD-L</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.2(4)E6,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-029fieldhouse-hightemp.net.utah.edu</td>
  <td>155.97.126.101</td>
  <td>Cisco</td>
  <td>WS-C3560X-24P-L</td>
  <td>C3560E-UNIVERSALK9-M</td>
  <td>12.2(55)SE3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-685madsen-206-1-clinical.net.utah.edu</td>
  <td>10.104.113.5</td>
  <td>Cisco</td>
  <td></td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.07.01.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-eeg-522wpav-w3235-clinical.net.utah.edu</td>
  <td>172.20.84.38</td>
  <td>Cisco</td>
  <td>WS-C3750X-48P-S</td>
  <td>C3750E-IPBASEK9-M</td>
  <td>15.0(2)SE10a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-eeg-525hosp-3043-clinical.net.utah.edu</td>
  <td>172.20.84.39</td>
  <td>Cisco</td>
  <td>WS-C3750X-48T-L</td>
  <td>C3750E-IPBASEK9-M</td>
  <td>15.0(2)SE10a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3648davishelipad-remote.net.utah.edu</td>
  <td>172.20.37.12</td>
  <td>Cisco</td>
  <td>WS-C3560CX-8PC-S</td>
  <td>C3560CX-UNIVERSALK9-M</td>
  <td>15.2(3)E1</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3110fs3-2155a-remote.net.utah.edu</td>
  <td>172.20.48.11</td>
  <td>Cisco</td>
  <td>WS-C3650-48PD-L</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-903westridge-l161-remote.net.utah.edu</td>
  <td>172.20.241.227</td>
  <td>Cisco</td>
  <td>WS-C4510R+E</td>
  <td>cat4500es8-UNIVERSALK9-M</td>
  <td>03.06.07.E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw1-3420pcsports-vpn.net.utah.edu</td>
  <td>172.29.5.81</td>
  <td>Cisco</td>
  <td></td>
  <td></td>
  <td>9.6(4)30</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r1-822fort-a04-lo.net.utah.edu</td>
  <td>172.29.254.1</td>
  <td>Cisco</td>
  <td>C9606R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.02,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>ddr2-ddc-j13.net.utah.edu</td>
  <td>172.29.1.23</td>
  <td>Cisco</td>
  <td>N7K-C7010</td>
  <td>n7000-s1-dk9</td>
  <td>6.2(16)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx3-ddc-g11.net.utah.edu</td>
  <td>172.28.65.121</td>
  <td>Cisco</td>
  <td>N9K-C93108TC-EX</td>
  <td>nxos</td>
  <td>7.0(3)I4(4)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx4-ddc-g11.net.utah.edu</td>
  <td>172.28.65.122</td>
  <td>Cisco</td>
  <td>N9K-C93108TC-EX</td>
  <td>nxos</td>
  <td>7.0(3)I4(4)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw-nephiairmed-1.med.utah.edu</td>
  <td>172.24.8.49</td>
  <td>Cisco</td>
  <td>ASA5506</td>
  <td></td>
  <td>9.8(4)10</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3574ddc-a4-pdu-ebc.net.utah.edu</td>
  <td>172.31.9.20</td>
  <td>Cisco</td>
  <td>WS-C2960X-24TS-L</td>
  <td>C2960X-UNIVERSALK9-M</td>
  <td>15.2(2)E7</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-0005.net.utah.edu</td>
  <td>172.30.132.4</td>
  <td>Cisco</td>
  <td>C9500-40X</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-0005csc-002c-park.net.utah.edu</td>
  <td>172.30.132.6</td>
  <td>Cisco</td>
  <td>C9300-24UX</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw-dixie-dental.med.utah.edu</td>
  <td>172.29.10.225</td>
  <td>Cisco</td>
  <td>ASA5506</td>
  <td></td>
  <td>9.8(4)8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-011wbb-400x-park.net.utah.edu</td>
  <td>172.30.134.137</td>
  <td>Cisco</td>
  <td>WS-C3650-48FQ-L</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-tdc-mgmt-16.net.utah.edu</td>
  <td>10.9.32.14</td>
  <td>Cisco</td>
  <td>C9300-48P</td>
  <td>CAT9K_IOSXE</td>
  <td>16.8.1a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx2-525hosp-4659-clinical.net.utah.edu</td>
  <td>172.20.64.14</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.4a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-525hosp-1443-clinical.net.utah.edu</td>
  <td>172.20.64.37</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-525hosp-a371-clinical.net.utah.edu</td>
  <td>172.20.64.17</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-provodialysis.net.utah.edu</td>
  <td>172.20.24.58</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.4a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-482-102tower-5344.net.utah.edu</td>
  <td>172.31.16.43</td>
  <td>Cisco</td>
  <td>WS-C3560CG-8PC-S</td>
  <td>C3560c405ex-UNIVERSALK9-M</td>
  <td>15.2(2)E9,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx3-0525hosp-cbnmgmt-b244-ebc.net.utah.edu</td>
  <td>172.29.1.103</td>
  <td>Cisco</td>
  <td>WS-C3650-24PD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-3704sjcn-1901a-sjcn.net.utah.edu</td>
  <td>172.20.49.5</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.9.2,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-3704sjcn-2400g-sjcn.net.utah.edu</td>
  <td>172.20.49.7</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.4</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-5150nrh-ll1-clin.net.utah.edu</td>
  <td>172.20.51.5</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.02,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw-liberty-dental.net.utah.edu</td>
  <td>172.29.12.137</td>
  <td>Cisco</td>
  <td>ASA5506</td>
  <td></td>
  <td>9.8(4)15</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3722shhc-3370-3722.net.utah.edu</td>
  <td>172.20.67.10</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r1-3722shhc-1225.net.utah.edu</td>
  <td>172.29.4.24</td>
  <td>Cisco</td>
  <td>C6816-X-LE</td>
  <td>c6848x-ADVENTERPRISEK9-M</td>
  <td>15.5(1)SY1</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r2-3722.net.utah.edu</td>
  <td>172.29.4.25</td>
  <td>Cisco</td>
  <td>C6816-X-LE</td>
  <td>c6848x-ADVENTERPRISEK9-M</td>
  <td>15.5(1)SY1</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3718unihome-3108-remote.net.utah.edu</td>
  <td>172.29.13.5</td>
  <td>Cisco</td>
  <td>C9407R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw-unphouse.net.utah.edu</td>
  <td>172.29.12.225</td>
  <td>Cisco</td>
  <td>ASA5506</td>
  <td></td>
  <td>9.8(4)12</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-851uuoc-1052-clinical.net.utah.edu</td>
  <td>172.20.28.14</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.6</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-525hosp-a0070-clinical.net.utah.edu</td>
  <td>172.20.64.62</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.9.4,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r1-services-179ebc-070.net.utah.edu</td>
  <td>172.29.1.32</td>
  <td>Cisco</td>
  <td>N77-C7710</td>
  <td>n7700-s2-dk9</td>
  <td>8.2(2)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r2-services-001park-150.net.utah.edu</td>
  <td>172.29.1.33</td>
  <td>Cisco</td>
  <td>N77-C7710</td>
  <td>n7700-s2-dk9</td>
  <td>8.2(2)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-5150nrh-1128-clin.net.utah.edu</td>
  <td>172.20.51.6</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.02,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx3-565eej-a610-ebc.net.utah.edu</td>
  <td>172.31.7.23</td>
  <td>Cisco</td>
  <td>WS-C3850-24XU-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>r2-822fort-a03-lo.net.utah.edu</td>
  <td>172.29.254.2</td>
  <td>Cisco</td>
  <td>C9606R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.02,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-179ebc-070-a7-services-services.net.utah.edu</td>
  <td>172.20.58.6</td>
  <td>Cisco</td>
  <td>C9300-24P</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.5</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-179ebc-070-ebc-new.net.utah.edu</td>
  <td>155.101.238.252</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.9.4,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-881hmhi-n2708-clinical.net.utah.edu</td>
  <td>172.20.242.175</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.6.6</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-114sch-004-5ar1-fort.net.utah.edu</td>
  <td>172.31.132.4</td>
  <td>Cisco</td>
  <td>WS-C3850-24XS-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx3-522wpav-w1665-clinical.net.utah.edu</td>
  <td>172.20.84.29</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.3a</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-587cmc-westcustodial-ebc.net.utah.edu</td>
  <td>172.31.0.73</td>
  <td>Cisco</td>
  <td>WS-C3650-24PS-L</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-881hmhi-n3708-clinical.net.utah.edu</td>
  <td>172.20.242.165</td>
  <td>Cisco</td>
  <td>C9410R</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.3a</td>
 </tr>
 <tr height=540 style='height:405.0pt;mso-xlrowspan:27'>
  <td height=540 colspan=6 style='height:405.0pt;mso-ignore:colspan'></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-0079sfebb-server-lib.net.utah.edu</td>
  <td>172.30.0.151</td>
  <td>Cisco</td>
  <td>N9K-C93180YC-FX</td>
  <td>nxos</td>
  <td>9.3(3)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx2-0079sfebb-server-lib.net.utah.edu</td>
  <td>172.30.0.152</td>
  <td>Cisco</td>
  <td>N9K-C93180YC-FX</td>
  <td>nxos</td>
  <td>9.3(3)</td>
 </tr>
 <tr height=40 style='height:30.0pt;mso-xlrowspan:2'>
  <td height=40 colspan=6 style='height:30.0pt;mso-ignore:colspan'></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-0079sfebb-100u-lib.net.utah.edu</td>
  <td>172.30.0.132</td>
  <td>Cisco</td>
  <td>C9500-48Y4C</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.02,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3536rosepark-h256-remote.net.utah.edu</td>
  <td>172.29.14.36</td>
  <td>Cisco</td>
  <td>WS-C3650-48FQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.9</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-0865-3042-clinical.net.utah.edu</td>
  <td>172.20.108.22</td>
  <td>Cisco</td>
  <td>C9300-48U</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.5b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw-3536rosepark-dental.net.utah.edu</td>
  <td>172.29.14.33</td>
  <td>Cisco</td>
  <td></td>
  <td></td>
  <td>9.8(2)38</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>fw-3582rocksprings-1mech.net.utah.edu</td>
  <td>172.29.20.241</td>
  <td>Cisco</td>
  <td>ASA5506</td>
  <td></td>
  <td>9.8(2)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-0036fmab-117-a1-lib.net.utah.edu</td>
  <td>172.30.8.228</td>
  <td>Cisco</td>
  <td></td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-876_375chipeta-sleepw-ebc.net.utah.edu</td>
  <td>172.31.11.138</td>
  <td>Cisco</td>
  <td>WS-C3650-48PQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-425-250plaza-493-remote.net.utah.edu</td>
  <td>172.29.2.233</td>
  <td>Cisco</td>
  <td>C9300-48P</td>
  <td>CAT9K_IOSXE</td>
  <td>17.3.3</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-425-250plaza-basement-remote.net.utah.edu</td>
  <td>172.29.2.240</td>
  <td>Cisco</td>
  <td>C9300-48P</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.5b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-weber-dental.net.utah.edu</td>
  <td>172.29.14.2</td>
  <td>Cisco</td>
  <td>WS-C3650-24PD-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.7,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dx1-3506ogdendental-comm-remote.net.utah.edu</td>
  <td>172.29.19.4</td>
  <td>Cisco</td>
  <td>WS-C3650-48FQ-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>03.06.06E<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx2-179ebc-070-a7-ebc.net.utah.edu</td>
  <td>172.29.1.55</td>
  <td>Cisco</td>
  <td>N9K-C93180YC-EX</td>
  <td>nxos</td>
  <td>9.2(4)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>dcx1-179ebc-070-a7-ebc.net.utah.edu</td>
  <td>172.29.1.54</td>
  <td>Cisco</td>
  <td>N9K-C93180YC-EX</td>
  <td>nxos</td>
  <td>9.2(4)</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-3716fhc-111-construction.net.utah.edu</td>
  <td>172.20.13.142</td>
  <td>Cisco</td>
  <td>WS-C3750X-48P-L</td>
  <td>C3750E-UNIVERSALK9-M</td>
  <td>15.0(2)SE6,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-482-102tower-nactest-4401.net.utah.edu</td>
  <td>172.31.16.26</td>
  <td>Cisco</td>
  <td>WS-C3850-48F-S</td>
  <td>CAT3K_CAA-UNIVERSALK9-M</td>
  <td>16.6.8</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-5100acc-a112a-clinical.net.utah.edu</td>
  <td>172.20.74.21</td>
  <td>Cisco</td>
  <td>C9300-24P</td>
  <td>CAT9K_IOSXE</td>
  <td>16.12.5b</td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx2-3716fhc-122-construction.net.utah.edu</td>
  <td>172.20.13.203</td>
  <td>Cisco</td>
  <td>WS-C2960S-24PS-L</td>
  <td>C2960S-UNIVERSALK9-M</td>
  <td>15.0(2)SE10,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-3716fhc-122-construction.net.utah.edu</td>
  <td>172.20.13.200</td>
  <td>Cisco</td>
  <td>WS-C2960S-48LPS-L</td>
  <td>C2960S-UNIVERSALK9-M</td>
  <td>15.0(2a)SE9</td>
 </tr>
 <tr height=40 style='height:30.0pt;mso-xlrowspan:2'>
  <td height=40 colspan=6 style='height:30.0pt;mso-ignore:colspan'></td>
 </tr>
 <tr height=20 style='height:15.0pt'>
  <td height=20 style='height:15.0pt'>sx1-029field-sign-lib.net.utah.edu</td>
  <td>155.97.126.102</td>
  <td>Cisco</td>
  <td>IE-4000-4GC4GP4G-E</td>
  <td>IE4000-UNIVERSALK9-M</td>
  <td>15.2(4)EA9,<span style='mso-spacerun:yes'> </span></td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=372 style='width:279pt'></td>
  <td width=117 style='width:88pt'></td>
  <td width=249 style='width:187pt'></td>
  <td width=148 style='width:111pt'></td>
  <td width=243 style='width:182pt'></td>
  <td width=472 style='width:354pt'></td>
 </tr>
 <![endif]>
</table>
</div>
</body>
</html>
