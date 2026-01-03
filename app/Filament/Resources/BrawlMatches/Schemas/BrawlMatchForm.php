<?php

namespace App\Filament\Resources\BrawlMatches\Schemas;

use Filament\Forms\Components\DateTimePicker;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Schema;

class BrawlMatchForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                TextInput::make('tournament_name')
                    ->required(),
                TextInput::make('team_a_id')
                    ->required()
                    ->numeric(),
                TextInput::make('team_b_id')
                    ->required()
                    ->numeric(),
                TextInput::make('score_a')
                    ->required()
                    ->numeric()
                    ->default(0),
                TextInput::make('score_b')
                    ->required()
                    ->numeric()
                    ->default(0),
                DateTimePicker::make('played_at')
                    ->required(),
            ]);
    }
}
