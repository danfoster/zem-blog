---
title: GPFS User Group Meeting 2015
category: sysadmin
tags: gpfs
---

The following post contains my notes from the [GPFS User Group meeting](http://www.gpfsug.org/may-2015-agenda/) in York.


## Keynote

*<sub>Doris Conti, Director, Spectrum Scale (GPFS) and HPC SW Product Development</sub>*

Doris' Keynote started the day with a theme that continued throughout the day:
IBM are encouraging their users to get in touch with developers to help steer
the direction of GPFS. They are also looking for customers to join Beta
programs for various components of GPFS.

## 4.1.1 Roadmap / High-level futures

*<sub>Scott Fadden</sub>*

First of all we received a friendly reminder of the new naming and it's
mapping: Spectrum Scale (GPFS) is part of Spectrum Storage. Spectrum control
can now manage / monitor Spectrum Scale.

GPFS 4.1.1 will be release in June 2015 and will contain the following new features:

* Asynchronous DR via AFM
* NFS 4.0
* SMB 3.0
* Openstack Cinder, Swift, mania support

GPFS 4.2 aims to be released in Q3 2015.

### The Protocols

GPFS is aiming to provide a single name space to: Client workstations, hardoop,
compute farm, user and applications. They provide this by providing a number of
access methods that they refer to as "The Protocols". These Include:

* POSIX
* NFS
* SMB/CIFS
* Map Reduce
* Openstack

A "Protcol Node" is a bundled software stack that aims to:

* Simplify the install process.
* Provide better locking (similar as CTDB does for CIFS) and failover management via the Cluster export services (CES).
* New performance tools and metrics. There will be new mmcommands for performance information. Will also provide a xymon interface.

#### NFS

Moving from the Kernel NFS server to Ganesha 2.2, a userland NFS server. This
move is for increased performance and the ability for GPFS to be able to fix
problems. The former is always a surprise to be, that a userland service can
perform better. But the latter could not come quick enough, the fact that GPFS has to resort to rebooting a node if it detects an NFS lock gives some insight to how problematic the kernel NFS server can be.

Ganesha also has good support for NFSv4 as well as NFSv3.

In some situations there is a group limit of 16 that needs to be addressed, it depends on the authentication protocol being used. IBM have a table for this somewhere.

#### Object

GPFS will provide a fully compliant Openstack Swift REST interface (PUT, POST, GET, DELETE).
There will also be an Amazon S3 protocol emulation layer for those users who require it.

#### SMB:

Based on samba 4.3
SMB2, SMB2.1
SMB3 support include manadatory features + SMB encryption

1000 groups per user
NFS, CIFS, GPFS cross-protocol locking
Rolling upgrade - no, 2 phase upgrade

directory notifcation - turned off by default. has performance impact.

                            | NFS                | Object         | SMB
---------------------------:|--------------------|----------------|----------
**Max # Protocol Nodes:**   | 32                 | 16             | 16
**Max # of "shares":**      | 100 exports        | 4M containers  | 1000 exports
**Max # of connections:**   | 4000-5000 / node   |                | 3000 / per node
**Max # of files:**         | 9 billion / FS     | 1 billion / FS | 9 billion / FS
**Rolling Upgrade?:**       | Yes                |                |




Destinations: Flash, disk, tape, storage tich servers, off premise (softlayer, multi-cloud storage toolkit).

### Client Experience

- Automating kernel module creation and installation

Immutable filesets

- Put in years ago for Integration archive (2007)
- new mmchfileset -m option - mode
-- regular
-- advistory : hardline is not allowed, directory can not be renamed or deleted un less empry.
-- non-compliant
-- compliant

### Other

fileset level backups with mmbackup
new preffered read option - read fastest
remote command execution - re-eval root ssh access. User level auth - can mail gpfs@us.ibm.com for scripts today.
speed-up inode expansion
allocate token manager momory on the fly  - shouldn't need to tune it anymore.
maintain disk descriptor on the fly, instead of just start. BIOS was trying to restore GPT partition is backup GTP partition was there and clobbering GPFS disk descriptior. GPFS also removes backup GPT partition tables again.

mmapplypolict --sort-command to use your own sort command

placement polict now default to first data pool

faster and more information when deleting bad/list disks
 - empty option does not scan for drained data
 - collect information on what files were affected:
 -   --inode-criteria criteriafile -o inoderesultfile
     prints interesting inodes,

 look at mmfileid

 will ESS be MLS complient? They have not been through the process, but would probably do it if someone asked.

# Failure Events, Recovery & Problem determination

##### *Scott Fadden*

Blame the networkk... and use nsdprtf to do it

* Works with TCP or RDMA
* Many to many
* Tests many parameters easily
* Does not require GPFS to be installed

nsdperf is in the sample directory - nsd protocol permance, not actual nsds.

nsdperf -s to fire it up, it's not secure!
nsdperf for interactive

netwrok admin with use iperf, 1-to-1, might work fine. Doesn't show many-to-many.

mmdiag --iohist - everyio, type, time etc


### Looking in to AFM

mmafmctl fs1 getstate
 - common question "my queue length is never zero, must not be synced", bmight just be read operations.
to see active operations: mmfsadm dump afm

afm stats in mmpmon


# Monitoring IBM Spectrum Scale using IBM Spectrum Control (VSC/TPC)

##### *Christian Bolik*

Spectrum Ctronol: aka IBM Tivoli Storage Productivity Center (TPC).

Provides improved visability into FC fabrics

Addressed by by Spectrum control (TPC 5.2.5)
* Which of my cluster are running out of free space
* which of my clusters or nodes havea health problem
* which file systems and pools and running out of capacity
* which file systems are mounted on which nodes
* how much space is occuptied by snapshots? are there any potentially obsolete ones?
* which quotas are close to being exceeded or have already been exceeded?
* which filesets are close to running out of free inodes?
* which nsds are at risk of becoming unavailable, or are unavailable?
* are the volumes backing my NSDs performing OK?
* are alll nodes fulfilling critical rolesi n the cluster and up and running

Periodic polling, not realtime. It's a daily collection process

Planned content in 5.2.6:
 * remote cluster mounted, which file systems are mounted from or by other clusters
 * ability to monitor GPFS cluster without requiring root credentials

Future:
* performance monitoring of most relevany metrics (node and file system I/O stats)
* Visability into Spectrium Scale objects, GNR, and AFM
* Provisioning of filesets, shares, nsds
* policy visability

How long is data kept? configurable, default is 3 months.
can it be dumped out? database schema views

Separately licenced product.

IBM storage management blog: ibm.co/172TdgH


# User Experience from University of Birmingham/CLIMB

##### *Simon Thompson*

Research Support do:
 - Research data storage and management
 - research data noetworking
 - visualisation
 - hpc
 - specialist projects (e.g. CLIMB)

HPC:
 - GPFS 4.1
 - 2 NSD servers
 - DS 3500 stoage arrays


If he could change one thing: I/O heat mapping
- gnr should support scalce out
- s3 hsm driver
- support write caching layer for small I/O
- finer grained user control

Research Data Storage:

Replicated across 2 data centres
seperate IB fabrics at each DC
10GbE links between DCs
Extedned SAN based - users  can buy space
designed and built in partnership with OCF
SAN over dark fibre.

Clients access a separate Samba cluster
plan to put a tape layer in.
How will samba play with HSM? Archive bit?
Powerfolder sync and share pilot - interesting to see how it wroks with GPFS.

GPFS - Openstack

allow usesrs to archive VMs and datasets. part of the archiving process.

Archiving in to a ceph cluster. How to do that automaticaly? Would be nice if there was a HSM S3 drvier.

They are using the cinder driver.

GPFS inside the VMs?
 - Want PSOIX style access to shared datasets, can't trust the VM, so GPFS, NFS not suitable.

# User Experience from NERSC

##### *Jason Hick*

NERSC has 21 different NFS server.

Utilization on group clusters was sporadic
ethernet interconnect was uder-provisioned


### Retired netapps filers by migrating data to HPSS archival storage
 - 21 Netapp filers, 7 years or older
 - users resistant at first, but were purprised at performance
 - Developed their own data management interface (JAMO) that moves data automatically between filesystem and archive

Introduced new GPFS scratch file system in Genepool cluster

Diverse workload
 * lots of chrun 100M KB-sized files per day and then deleting them
     -have not address that yet
     - especially challenging with use of snapshots and quota
* users questing 10 GBs / sec bandside
    - use separate filesystem 
* proudction filesystem

Enabled Disaster protections:
- enabled GPFS snapshots
- backup to HPSS
   - custom software (PIBS) to perform incremental backups on PB-sized filesystems

       TCP kernel setting:
        need smaller initial send buffers

prevent head-of-line blocking - saw congestion like symptoms without congestion traffic.

They preferred DEbian and initially used Debian 5 with GPFS 3.3
 - high degree of expels - memory errors causing GPFS asserts
Switched to Debian 6 with GPFS 3.4 - all memory errors ceased, reduced the number of expels

Move from eithernet to IB:
 - IB expels much less frequent, performance more consistent. But have routing/topology challenges.

     data 1PB
     seq 0.5PB
     projectb 2.5PB - scratch

scheduler upgrade/enhancements: consider better features for job deps
workflow software: help manage work external to compute

data management tools: SRM/BeStMan, iRODS, GPFS Policy Manager


# AFM & Async DR Use Cases

##### *Shankar Balasubramanian*

DR for spectrum scale
* file level async replication of data using AF
* active passive model
* strict 1-1 relationship between primary and secondary
* supports nfsv3 and GPFS bacnend protocol for primary to secondary communication
* supports RPO

only works on GPFS independent filesets

no way of having multiple secondaries

primary is an AFM cache fileset
secondary if AFM home filesete
can be created independantly
only the priary can write to the secondary - it's RO for the rest of the world
data flows always from primary to secondary
primary is continuously accessable even when secondary is not accessible
PROs are maintained using peer-peer snapshots between primary and secondary
failover to secondary is done by upgraing the secondary to a primary (acting primary)
failback to old primary is done through a downgrade of acting primary to secondary


cannot go back more than 2 snapshots (is this really true?!)
15 mins is the default snapshot period.
async delay is tunable

RPO misses:
 - RPO is missed due ot network delay
     AFM_PRO_MISS
     mmaddcallback to reister event handling script.

     check every 5 mins if the RPO is still in the gateway queue

## Use cases

HSM support not in the first release.

Railure recovert

failback, create a ...

Avail in 4.1.1


# mmbackup + TSM Integration


##### *Stefan Bender*

bob: mmigmbackup - backup metadata

stefan.bender@de.ibm.com

mmbackup
- musch faster file system scanning time allows tsm backups to scale to many more objects compared to tsm progressive incremential

    cycle:
    start mmbackup
    use existing shadow DB or query TSM server to generate a new shadow database
    perform filesystem scan
    compare scan reults and shadow database
    perform expire / upgrade / send by using the TSM CA CLI
    backup shadow DB

3.5 TL3 updates:
* new shadow DB debian,
*    - reduce number of sort() interations to inlucde performance
*    - allow paraellel update on the shadow DB
*    - restartable backups - shadow db shows current prgoress and work remaining
*    - elimination of the post processing phase
*    - improved failure detection for TSM failures
*
* exploit incremental backup function
 - detect CTIME changes withdata or MTIME changes and run incremental
 -  CTIME, owner, group mode change - run dsmc incremental
 -  MTIME or file size change - run dsmc selective
 -  detech HSM migration changes
 -   - migration state change only - run gsmc incremental

ACL or extended atrributes changes are considered file changes in TSM eyes

4.1 updates

improved env verification

* verify filesystem is mounted
* verify TSM BA client is installed
* verify TSM CA client version is qual on all nodes
* verify a session with a TSM server can be established
* verify helper tool version is correct
* verify TSM options are set
    - QUOTESARELITERAL (use with mmbackup --noquotes)
    - SKIPACL

mmbackup options  - TSM
--max-backup-size - TXBYTELIMIT
max-backout-count max-expire-count  - TXGROUPMAX
expire-threads
backup -threads - (TSM BA client: RESOURCEUTILIZATION) - MAXSESSION MAX

mmbackup options for maax-backup-size should be larger than TSM server. TSM server will chunk it in to batches.

TSM CA client file list expiration processing importved in TSM 6.4.1 - can do multiple expirations per transactions (currently only 1)

TSM include and exclude options hay have significant impact on scan performance.

iuse as few EXCLUDE as possible
avaoid using INCLUDE. use exclude instead
do not use EXCLUDE /dir/.../*, use EXCLUDE.DIR instead
do not combine exclude and include for one subtree
if include is only used to assign right management class in TSM, use mmbackup service flag is used 

serialize backups of different file systems!

charabter limitations:
 files with ctrl=x, ctrl-y , carriage return adn the new line char in their canme can't be backup up to TSM
 use QUOTESARELITERAL if file names cantain " or '
 use WILDCARDSARELITERAL if file names contain * or ?)

# IBM Spectrum Scale (formerly GPFS) performance update, protocol performance and sizing

##### *Sven Oehme*

average: 1 bit flip per 1PB
GNE end-to-end ingtegraty checking prevents this.

baseline testing: ior:

api: POSIX
access: file-per-rocess
ordering in a file = requential offsets
order inter file = no tasks offsets
clients = 32 (4 per node)
repetiations = 100
xfersize = 1MiB
blocksize = 128 GiB
aggregate filesize = 4096 GiB

GS4-SSD becnhmark results:

filesystem blocksize    write MB/sec    read
1 MB                    17139           20858
4                       18205           26110
8                       19201           24457

GS4-SAS:
1                       1709            3029
4                       4039            6715
8                       4665           7666
16                      5619          8858 

at least 4MB block size for most new filesystems. since it's not much waste with <4kb files being stored in inodes.

NSD server can do 200,000 iops. Will go up to 350,000 in 4.1.1

big improvements in performance between 3.4 to 3.5 and even more to 4.1

scatter vs cluster. scatter does't slow down as much with full filesystems.

USing GL2-NSSAS as TSM backend: get 5Gb/s


