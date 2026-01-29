from typing import List, Dict
def chunk(data:Dict)->List[Dict]:
    chunks = []
    #command is now stored as a single self-contained chunk due to which code-> 
    #has been bigger
    def format_list(items, prefix="- "):
        return "\n".join(f"{prefix}{i}" for i in items)

    for cmd in data.get("commands", []):
        command_name = cmd.get("command")
        text = f"""
                Command: {command_name}
                Category: {cmd.get('category')}
                Syntax: {cmd.get('syntax')}
                Description: {cmd.get('description')}
                Detailed Explanation: {cmd.get('detailed_explanation')}
                """
        chunks.append({
            "text": text,
            "metadata": {
                "type": "command_core",
                "command": command_name,
                "category": cmd.get("category"),
                "skill_level": cmd.get("skill_level")
            }
        })

        if cmd.get("common_options"):
            text = f"Command: {command_name}\n\nCommon options:\n"
            for opt in cmd["common_options"]:
                text += f"- {opt['option']}: {opt['description']}\n"

            chunks.append({
                "text": text.strip(),
                "metadata": {
                    "type": "command_options",
                    "command": command_name
                }
            })

        if cmd.get("permission_modes"):
            text = f"Command: {command_name}\n\nPermission modes:\n"
            for mode in cmd["permission_modes"]:
                text += f"\n{mode['type']} mode examples:\n"
                for ex in mode["examples"]:
                    text += f"- {ex}\n"

            chunks.append({
                "text": text.strip(),
                "metadata": {
                    "type": "command_modes",
                    "command": command_name,
                    "mode_type": "permissions"
                }
            })

        if cmd.get("modes"):
            text = f"Command: {command_name}\n\nModes:\n"
            for m in cmd["modes"]:
                text += f"- {m['mode']} ({m['key']}): {m['description']}\n"

            chunks.append({
                "text": text.strip(),
                "metadata": {
                    "type": "command_modes",
                    "command": command_name
                }
            })

        if cmd.get("common_expressions"):
            text = f"Command: {command_name}\n\nCommon expressions:\n"
            for exp in cmd["common_expressions"]:
                text += f"- {exp['expression']}: {exp['description']}\n"

            chunks.append({
                "text": text.strip(),
                "metadata": {
                    "type": "command_expressions",
                    "command": command_name
                }
            })
        if cmd.get("examples"):
            chunks.append({
                "text": f"Command: {command_name}\n\nExamples:\n" + format_list(cmd["examples"]),
                "metadata": {
                    "type": "command_examples",
                    "command": command_name
                }
            })

        if cmd.get("security_considerations"):
            chunks.append({
                "text": f"Command: {command_name}\n\nSecurity considerations:\n{cmd['security_considerations']}",
                "metadata": {
                    "type": "command_security",
                    "command": command_name
                }
            })

    for guide in data.get("installation_guides", []):
        title = guide.get("title")
        guide_id = guide.get("guide_id")

        base_meta = {
            "type": "installation_guide",
            "guide_id": guide_id,
            "title": title,
            "skill_level": guide.get("skill_level")
        }
        overview = [
            f"Installation Guide: {title}",
            f"Skill Level: {guide.get('skill_level')}",
            f"Overview: {guide.get('overview')}"
        ]

        chunks.append({
            "text": "\n".join(overview),
            "metadata": {**base_meta, "section": "overview"}
        })

        if guide.get("prerequisites"):
            prereq = ["Prerequisites:"]
            for item in guide["prerequisites"]:
                prereq.append(f"- {item}")

            chunks.append({
                "text": f"Installation Guide: {title}\n" + "\n".join(prereq),
                "metadata": {**base_meta, "section": "prerequisites"}
            })

        if guide.get("steps"):
            steps = ["Installation Steps:"]
            for idx, step in enumerate(guide["steps"], 1):
                steps.append(f"{idx}. {step}")

            chunks.append({
                "text": f"Installation Guide: {title}\n" + "\n".join(steps),
                "metadata": {**base_meta, "section": "steps"}
            })

        if guide.get("common_distributions"):
            distros = ["Common Linux Distributions:"]
            for distro in guide["common_distributions"]:
                distros.append(f"- {distro}")

            chunks.append({
                "text": f"Installation Guide: {title}\n" + "\n".join(distros),
                "metadata": {**base_meta, "section": "distributions"}
            })

        if guide.get("post_installation_steps"):
            post = ["Post-Installation Steps:"]
            for step in guide["post_installation_steps"]:
                post.append(f"- {step}")

            chunks.append({
                "text": f"Installation Guide: {title}\n" + "\n".join(post),
                "metadata": {**base_meta, "section": "post_install"}
            })

        if guide.get("troubleshooting"):
            trouble = ["Troubleshooting:"]
            for issue in guide["troubleshooting"]:
                trouble.append(f"- {issue}")

            chunks.append({
                "text": f"Installation Guide: {title}\n" + "\n".join(trouble),
                "metadata": {**base_meta, "section": "troubleshooting"}
            })

        if guide.get("security_notes"):
            security = ["Security Notes:"]
            for note in guide["security_notes"]:
                security.append(f"- {note}")

            chunks.append({
                "text": f"Installation Guide: {title}\n" + "\n".join(security),
                "metadata": {**base_meta, "section": "security"}
            })
    
    for concept in data.get("linux_fundamentals", []):
        topic = concept.get("topic")
        topic_id = concept.get("topic_id")

        base_meta = {
            "type": "linux_fundamental",
            "topic": topic,
            "topic_id": topic_id
        }

        overview = [
            f"Linux Concept: {topic}",
            f"Description: {concept.get('description')}"
        ]

        chunks.append({
            "text": "\n".join(overview),
            "metadata": {**base_meta, "section": "overview"}
        })

        if concept.get("directories"):
            dirs = ["Linux File System Directories:"]
            for d in concept["directories"]:
                dirs.append(f"- {d['path']}: {d['description']}")

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(dirs),
                "metadata": {**base_meta, "section": "directories"}
            })

        if concept.get("key_concepts"):
            keys = ["Key Concepts:"]
            for item in concept["key_concepts"]:
                keys.append(f"- {item}")

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(keys),
                "metadata": {**base_meta, "section": "concepts"}
            })

        if concept.get("permission_bits"):
            bits = ["Permission Bits:"]
            for bit in concept["permission_bits"]:
                bits.append(
                    f"- {bit['bit']} ({bit['value']}): "
                    f"File → {bit['file_meaning']}, "
                    f"Directory → {bit['directory_meaning']}"
                )

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(bits),
                "metadata": {**base_meta, "section": "permission_bits"}
            })

        if concept.get("special_permissions"):
            sp = ["Special Permissions:"]
            for perm in concept["special_permissions"]:
                sp.append(f"- {perm['permission']}: {perm['description']}")

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(sp),
                "metadata": {**base_meta, "section": "special_permissions"}
            })

        if concept.get("process_states"):
            states = ["Process States:"]
            for s in concept["process_states"]:
                states.append(f"- {s}")

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(states),
                "metadata": {**base_meta, "section": "process_states"}
            })

        if concept.get("process_attributes"):
            attrs = ["Process Attributes:"]
            for a in concept["process_attributes"]:
                attrs.append(f"- {a}")

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(attrs),
                "metadata": {**base_meta, "section": "process_attributes"}
            })

        if concept.get("operators"):
            ops = ["Operators and Redirection:"]
            for op in concept["operators"]:
                ops.append(
                    f"- {op['operator']} ({op['name']}): "
                    f"{op['description']} | Example: {op['example']}"
                )

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(ops),
                "metadata": {**base_meta, "section": "operators"}
            })
        if concept.get("streams"):
            streams = ["Standard Streams:"]
            for s in concept["streams"]:
                streams.append(f"- {s['stream']}: {s['description']}")

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(streams),
                "metadata": {**base_meta, "section": "streams"}
            })

        if concept.get("related_commands"):
            rel = ["Related Commands:"]
            for cmd in concept["related_commands"]:
                rel.append(f"- {cmd}")

            chunks.append({
                "text": f"Linux Concept: {topic}\n" + "\n".join(rel),
                "metadata": {**base_meta, "section": "related_commands"}
            })
    
    for guide in data.get("troubleshooting_guides", []):
        text = f"Issue: {guide.get('issue')}\n\n"

        if guide.get("diagnosis"):
            text += "Diagnosis steps:\n"
            for step in guide["diagnosis"]:
                text += f"- {step}\n"

        if guide.get("resolution"):
            text += "\nResolution steps:\n"
            for step in guide["resolution"]:
                text += f"- {step}\n"

        if guide.get("related_commands"):
            text += "\nRelated commands: "
            text += ", ".join(guide["related_commands"])

        chunks.append({
            "text": text.strip(),
            "metadata": {
                "type": "troubleshooting",
                "issue": guide.get("issue"),
                "commands": guide.get("related_commands", [])
            }
        })

    
    for scenario in data.get("common_scenarios", []):
        text = f"Scenario: {scenario.get('title')}\n"
        text += f"Description: {scenario.get('description')}\n\n"

        if scenario.get("tasks"):
            text += "Tasks:\n"
            for task in scenario["tasks"]:
                text += f"- {task}\n"

        if scenario.get("command_sequence"):
            text += f"\nCommand sequence:\n{scenario['command_sequence']}"

        chunks.append({
            "text": text.strip(),
            "metadata": {
                "type": "scenario",
                "scenario_id": scenario.get("scenario_id"),
                "title": scenario.get("title")
            }
        })

    
    for pkg in data.get("package_managers", []):
        text = f"Package Manager: {pkg.get('name')}\n"
        text += f"Supported distributions: {', '.join(pkg.get('distributions', []))}\n\n"

        if pkg.get("common_commands"):
            text += "Common commands:\n"
            for cmd in pkg["common_commands"]:
                text += f"- {cmd}\n"

        chunks.append({
            "text": text.strip(),
            "metadata": {
                "type": "package_manager",
                "name": pkg.get("name"),
                "distributions": pkg.get("distributions", [])
            }
        })
    return chunks

# print(f"Created {len(chunks)}")
# print(chunks[3])